from . import pygments_override
from . import switcher
from . import translator

import sphinx.environment
try:
    from sphinx.environment.adapters import toctree
except ImportError:
    toctree = None

import sphinx.builders.html
from sphinx import addnodes
from docutils import nodes


def setup(app):
    if hasattr(app, 'set_translator'):
        app.set_translator('html', translator.BootstrapTranslator)
    else:
        if getattr(app.config, 'html_translator_class', None):
            app.warn("Overriding the explicitly set html_translator_class setting",
                     location="odoo extension")
        app.config.html_translator_class = 'odoo_ext.translator.BootstrapTranslator'

    switcher.setup(app)
    app.add_config_value('odoo_cover_default', None, 'env')
    app.add_config_value('odoo_cover_external', {}, 'env')
    app.add_config_value('odoo_cover_default_external', lambda conf: conf.odoo_cover_default, 'env')
    app.connect('html-page-context', update_meta)


def update_meta(app, pagename, templatename, context, doctree):
    meta = context.get('meta')
    if meta is None:
        meta = context['meta'] = {}
    meta.setdefault('banner', app.config.odoo_cover_default)

class monkey(object):
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, fn):
        name = fn.__name__
        old = getattr(self.obj, name)
        setattr(self.obj, name, lambda self_, *args, **kwargs: \
                fn(old, self_, *args, **kwargs))

@monkey(toctree.TocTree)
def resolve(old_resolve, tree, docname, *args, **kwargs):
    resolved_toc = old_resolve(tree, docname, *args, **kwargs)
    if resolved_toc:
        # Not sure set_class really does what we want.
        _toctree_add_empty_class(tree, resolved_toc, docname)
        resolved_toc['classes'].append('testtesttest')
    return resolved_toc

def _toctree_add_empty_class(tree, node, docname) -> None:
    for subnode in node.children:
        if isinstance(subnode, (
            addnodes.compact_paragraph,
            nodes.list_item,
            nodes.bullet_list
        )):
            # for <p>, <li> and <ul> just recurse
            _toctree_add_empty_class(tree, subnode, docname)
        elif isinstance(subnode, nodes.reference):
            toc_ref = get_reference(subnode, docname)
            if toc_ref and 'empty_page' in tree.env.metadata[toc_ref]:
                subnode['classes'].append('o_empty_page')

def get_reference(node, docname):
    ref = node['refuri'].replace('.html', '') # applications.html
    if ref.find('..') < 0:
        # direct reference
        return ref
    splitted_refuri = ref.split('/')
    count = 0 # Number of ../ in refuri
    for split in splitted_refuri:
        if split == "..":
            count += 1
    # ref = ../../../contributing/documentation
    # docname = services/legal/terms/enterprise
    # res = contributing/documentation
    res = docname.split('/')[:-(count+1)] + splitted_refuri[count:]
    return "/".join(
        res
    )
