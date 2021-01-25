====
Peru
====

Introduction
============

The Argentinean localization has been improved and extended in Odoo v13, in this version the next
modules are available:

- **l10n_pe**: Adds accounting features for the Peruvian localization, which represent the minimal
  configuration required for a company to operate in Peru and under the SUNAT regulations and 
  guidelines. The main elements included in this module are: Chart of account, taxes, 
  document types. 


- **l10n_pe_edi**: ncludes all technical and functional requirements to generate and validate 
  Electronic Invoice, based on the SUNAT specification to create and process valid electronic 
  documents, for more technical detail you can access this reference.  
  `SUNAT <https://cpe.sunat.gob.pe/node/88/>`_, that keeps track of new changes and updates.  
  The features of this module are based on the resolutions published on the 
  `SUNAT Legislation <https://www.sunat.gob.pe/legislacion/general/index.html/>`_.

Configuration
=============

Install the Peruvian localization modules
-----------------------------------------

For this, go to *Apps* and search for Peru. Then click Install in the module Peru EDI, this 
module has a dependency with Peru - Accounting in case this last one is not installed, Odoo 
installs it automatically within EDI.

.. image:: media/peru_01_modules.png
   :align: center
   :alt: Modules

.. note::
   When you install a database from scratch selecting Peru as country, Odoo will automatically 
   install the base module: Peru - Accounting.


Configure your company
~~~~~~~~~~~~~~~~~~~~~~

In addition to the basic information in the Company,  we need to set Peru as the Country, this 
is essential for the Electronic Invoice to work properly.  The field Address Type Code, 
represents the establishment code assigned by the SUNAT when companies register their RUC 
Unique Contributor Registration):

.. image:: media/peru_02_company.png
   :align: center
   :alt: Company data


.. tip::
   In case the Address type code is unknown,  you can set it as default value: 0000. Be aware 
   that if an incorrect value is entered, the Electronic invoice validation might have errors. 
 
.. note::
   The NIF should be set following the RUC format.

   
Chart of Account
~~~~~~~~~~~~~~~~

The chart of accounts is installed by default as part of the set of data included in the 
localization module, the accounts are mapped automatically in: 

- Taxes
- Default Account Payable.
- Default Account Receivable

The chart of accounts for Peru is based on the most updated version of the PCGE (Plan Contable 
General Empresarial) which is grouped in several categories and is compatible with NIIF 
accounting.

Accouting Seetings
------------------
Once the modules are installed and the basic information of your company is set, you need to 
configure the elements required for Electronic Invoice, for this you can access to 
:menuselection:`Accounting --> Settings --> Peruvian Localization`

Basic Concepts
~~~~~~~~~~~~~~
Here are some terms that are essential on the Peruvian localization: 

- **EDI**: Electronic Data Interchange, which in this refers to the Electronic Invoice. 
- **SUNAT**: is the organization which enforces customs and taxation in Peru.
- **OSE**: Electronic Service Operator (Operador de Servicios Electrónicos),
    `SUNAT Reference <https://cpe.sunat.gob.pe/aliados/ose#:~:text=El%20Operador%20de%20Servicios%20Electr%C3%B3nicos%20(OSE)%20es%20qui%C3%A9n%20se%20encarga,otro%20documento%20que%20se%20emita>`_.
- **CDR**: Receipt certificate (Constancia de Recepción) 
- **SOL Credentials**: User and password provided by the SUNAT and grants access to Online Operations systems. 


Signature Provider
~~~~~~~~~~~~~~~~~~
As part of  the requirements for Electronic Invoice is Peru, your company need 
to select a Signature Provider, that will take care of the document signing process 
and to manage the SUNAT validation response , Odoo offers three options:

#. IAP (Odoo In App Purchase)
#. Digiflow
#. SUNAT

Please refer to the sections belows to check the details and considerations for each option.

IAP (Odoo In App Purchase)
**************************
This is the default and the suggested option in Odoo estadard, as you don’t need to have a 
certificate or a signature.

.. image:: media/peru_03_IAP.png
   :align: center
   :alt: IAP
   
**What is the IAP?**
This is a signature service offered directly by Odoo, the service takes care of the next process: 
#. Provides the Electronic invoice Certificate, so you do not need to acquire one by yourself.
#. Send the document to the OSE , in this case Digiflow.
#. Receive the OSE validation and CDR.

**How does it work?**
The service requires Credits in order to process your electronic documents. Odoo will provide 
1000 credits for free in new databases, after these credits are consumed you need to buy a 
Credit Package. 

| Credits | EUR |
|---------|-----|
| 1000    | 22  |
| 5000    | 110 |
| 10000   | 220 |
| 20000   | 440 |


The credits are consumed per each document that is sent to the OSE. 

.. important::
   In case that you have a validation error and the document needs to be sent one more time, and 
   additional credit will be charged, so it’s paramount that before sending your document to the 
   OSE you verify all information is correct.

**What do you need to do?**

- In Odoo, once your enterprise contract is activated and you start working in Production, you 
  will need to buy credits once the first 1000 are consumed.

- As Digiflow is the OSE used in the IAP,  you will need to affiliate it as the official OSE for 
  your company in the SUNAT website, this is a simple process. For more information please check 
  the: `Next manual <https://drive.google.com/file/d/1BkrMTZIiJyi5XI0lGMi3rbMzHddOL1pa/view?usp=sharing>`_.
   
Digiflow
********
This option can be used as an alternative, instead of using the IAP services you can send your 
document validation directly to Digiflow. In this case you will need to consider:


- Buy your own electronic Certificate: For more detail regarding the official list of certificate 
  provides and the process to acquire it, please refer to the next reference  
  `SUNAT <https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/>`_.
- Sign a service agreement directly with `Digiflow <https://www.digiflow.pe/>`_.
- Provide your SOL credentials.

.. image:: media/peru_04_Digiflow.png
   :align: center
   :alt: Digiflow

SUNAT
*****
In case your company wants to sign directly with the SUNAT, it is possible to select this option 
in your configuration. In this case you will need to consider:
- Get the SUNAT Certification process accepted.

- Buy your own electronic Certificate: For more detail regarding the official list of certificate 
  provides and the process to acquire it, please refer to the next reference  
  `SUNAT <https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/>`_.
  
- Provide you SOL credentials. 


Testing environment
~~~~~~~~~~~~~~~~~~~
Odoo provides a testing environment that can be activated before your company goes to production. 

When using the testing environment and the IAP signature, you don’t need to buy testing credits 
for your transactions as all of them are validated by default.

.. tip::
   By default the databases are set to work on production, make sure to enable the testing mode 
   if needed. 

Certificate
~~~~~~~~~~~
In case you  don’t use Odoo IAP, in order to generate the electronic invoice signature, a digital 
certificate with extension (.pfx) is required, proceed to this section and load your 
file and password.

.. image:: media/peru_05_Certificate.png
   :align: center
   :alt: Certificate
   
Multicurrency
~~~~~~~~~~~~~
The official currency exchange rate in Peru is provided by the Bank of Peru. Odoo can connect 
directly to its services and get the currency rate either automatically or manually.

.. image:: media/peru_06_multicurrency.png
   :align: center
   :alt: Multicurrency Service
   
Please refer to the next section in our documentation for more information about 
`Multicurrency <https://www.odoo.com/documentation/user/14.0/accounting/others/multicurrencies/how_it_works.html>`_.


Configure Master data
---------------------

Taxes
~~~~~
As part of the localization module the taxes are created automatically with their related 
financial account and electronic invoice configuration.

.. image:: media/peru_07_taxes.png
   :align: center
   :alt: Taxes list

EDI Configuration
*****************
As part of the taxes configuration, there are three new fields required for electronic invoice, 
the taxes created by default have this data included, but in case you create new taxes make 
sure you fill in the fields: 

.. image:: media/peru_08_taxes_edi.png
   :align: center
   :alt: Taxes EDI data


Fiscal Positions
~~~~~~~~~~~~~~~~
There are two main fiscal positions included by default when you install the Peruvian localization.

**Extranjero - Exportación**: Set this fiscal position on customers for Exportation transactions.

**Local Peru**: Set this fiscal position on local customers.

Document Types
~~~~~~~~~~~~~~
In some Latin American countries, including Peru, some accounting transactions like invoices and 
vendor bills are classified by document types, defined by the government fiscal authorities, in 
this case by the SUNAT. 

Each document type can have a unique sequence per journal where it is assigned. As part of the 
localization, the Document Type includes the country on which the document is applicable;the data 
is created automatically when the localization module is installed.
 
The information required for the document types is included by default so the user does not need 
to fill anything on this view:

.. image:: media/peru_09_document_type.png
   :align: center
   :alt: Document Type


Journals
~~~~~~~~
Additional to the standard fields on the Journals,for the Peruvian localization When creating 
sales journals the next information must be filled in: 

Use Documents 
*************
This field is used to define if the journal will use Document Types, it’s only applicable on 
Purchase and Sales journals which are the ones that can be related to the different set of 
document types available in Peru. By default all the sales journals created use documents. 

Electronic Data Interchange
***************************
This  section indicates which EDI workflow is used in the invoice, for Peru we must select 
“Peru UBL 2.1”.

.. image:: media/peru_10_id_type.png
   :align: center
   :alt: Journal EDI

.. tip::
  By default the value Factur-X (FR) is always displayed but you can unchecked it manually.  

Partner
~~~~~~~

Identification Type and VAT
***************************
As part of the Peruvian localization, the identification types defined by the SUNAT are now 
available on the Partner form, this information is essential for most transactions either on 
the sender company and in the customer, make sure you fill in this information in your records.

.. image:: media/peru_10_id_type.png
   :align: center
   :alt: Partner identification type


Product
~~~~~~~
Additional to the basic information in your products, for the Peruvian localization, the UNSPC 
Code on the product is a suggested value to be configured. 

.. image:: media/peru_11_unspc_code.png
   :align: center
   :alt: UNSPC Code


Usage and testing
=================

Customer invoice
----------------

EDI Elements
~~~~~~~~~~~~
Once you have configured your master data, the invoices can be created from your sales order or
manually, additional to basic invoice information described in 
`this section  <https://www.odoo.com/documentation/user/14.0/accounting/receivables/customer_invoices/overview.html/>`_
there are a couple of fields required as part of the Peru EDI: 


- **Document type**: The default value is “Factura Electronica” but  you can manually change the 
  document type if needed and select Boleta for example. 

.. image:: media/peru_12_document_type.png
   :align: center
   :alt: Invoice document type

- **Operation type**: This value is required for Electronic Invoice and indicates the transaction 
  type, the default value is “Internal Sale” but another value can be selected manually when needed, 
  for example Export of Goods. 

.. image:: media/peru_13_operation_type.png
   :align: center
   :alt: Invoice operation type

- **EDI Affectation Reason**: In the invoice lines, you will notice that additional to the Tax 
  there is a field “EDI Affectation Reason” that determines the tax scope based on the SUNAT list 
  that is displayed. All the taxes loaded by default are associated with a default EDI affection 
  reason, if needed you can manually select another one when creating the invoice.  

.. image:: media/peru_14_tax_affectation_reason.png
   :align: center
   :alt: Tax affectation reason


Invoice validation
~~~~~~~~~~~~~~~~~~

Once you check all the information in your invoice is correct you can proceed to validate it, 
this action registers the account move in the accounting and triggers the Electronic invoice 
workflow to send it to the OSE and the SUNAT, the next message is displayed at the top of the 
invoice:

.. image:: media/peru_15_posted_invoice.png
   :align: center
   :alt: EDI invoice sending

Asynchronous means that the document is not sent automatically after the invoice has been posted. 


Electronic Invoice Status
*************************
**To be Sent**: To be sent: Indicates the document is ready to be sent to the OSE, this can be 
done either automatically by Odoo with a cron that runs every hour,  or the user can send it 
immediately by clicking on the button “Sent now”.

.. image:: media/peru_15_sent_manual.png
   :align: center
   :alt: Send EDI manually


**Sent**: Indicates the document was sent to the OSE and was successfully validated. As part of 
the validation a ZIP file is downloaded and a message is logged in the chatter indicating the 
correct Government validation.  

.. image:: media/peru_16_invoice_sent.png
   :align: center
   :alt: Send EDI manually

In case there is a validation error the Electronic Invoice status remains in “To be sent” so the 
corrections can be made and the invoice can be sent again. 

.. warning::
   One credit is consumed each time that you send a document for validation, in this sense if an 
   error is detected on an invoice and you send it one more time, two credits are consumed in total.


Common Errors
~~~~~~~~~~~~~
There are multiple reasons behind a rejection from the OSE or the SUNAT, when this happens Odoo 
sends a message at the top of the invoice indicating the error details and in the most common 
cases a hint to fix the issue. 

If a validation error is received, you have two options: 

* In case the error is related to master data on the partner, customer or taxes you can simply 
  apply the change on the record (example customer identification type) and once it is done click 
  on the Retry button. 
* If the error is related to some data recorded on the invoice directly (Operation type, missing 
  data on the invoice lines) the correct solution is Reset the invoice to Draft, apply the changes 
  and then send the invoice again to the SUNAT for another validation. 

.. image:: media/peru_17_errors.png
   :align: center
   :alt: Invoice errors


For more detail regarding the common errors you might have please refer to 
`this link  <https://www.nubefact.com/codigos-error-sunat/>`_


Invoice PDF Report
~~~~~~~~~~~~~~~~~~
After the invoice is Accepted and validated by the SUNAT and the PDF is printed it includes the 
fiscal elements that indicates out document is fiscally valid:

.. image:: media/peru_18_PDF.png
   :align: center
   :alt: Invoice PDF report


IAP Credits
~~~~~~~~~~~
Odoo’s Electronic IAP offers 1000 credits for free, after these credits are consumed in your 
production database, your company must buy new credits in order to process your transactions. 

Once you run out of credits a red label will appear at the top of the invoice indicating that 
additional credits are required, you can easily buy them by accessing the link provided in 
the message. 

.. image:: media/peru_19_credits_IAP.png
   :align: center
   :alt: Buying credits in the IAP

In the link you will find several packages with different pricing based on the number of credits. 
The price list in the IAP is always displayed in EUR.



Special Use cases
~~~~~~~~~~~~~~~~~

Cancelation process
*******************
There are some scenarios that require an invoice cancellation, example when an invoice was created 
by mistake. If the invoice was already sent and validated by the SUNAT, the correct way to proceed 
is by clicking on the button Request Cancellation:

.. image:: media/peru_20_cancellation.png
   :align: center
   :alt: Request cancellation

In order to cancel an invoice you will need to provide a cancellation Reason. 


Electronic Invoice Status
^^^^^^^^^^^^^^^^^^^^^^^^^
**To Cancel**:  Indicates the cancellation request is ready to be sent to the OSE, this can be done 
either automatically by Odoo with a cron that runs every hour, or the user can send it 
immediately by clicking on the button “Send now”. Once it is sent, a cancellation ticket is 
created, as a result the next message and CDR File are logged in the chatter:

.. image:: media/peru_21_cancellation_cdr.png
   :align: center
   :alt: Cancellation CDR
   
**Cancelled**: Indicates the cancellation request was sent to the OSE and was successfully 
validated. As part of the validation a ZIP file is downloaded and a message is logged in the 
chatter indicating the correct Government validation.

.. image:: media/peru_22_cancelled.png
   :align: center
   :alt: Canceled invoice

.. warning::
   One credit is consumed on each cancellation request.
   
Cancelation process
*******************
When creating exportation invoices, take into account the next considerations:

- The Identification type on your customer must be Foreing ID. 
- Operation type in your invoice must be an Exportation one. 
- The taxes included in the invoice lines should be EXP taxes.

.. image:: media/peru_23_exp_invoice.png
   :align: center
   :alt: Exportation invoices

Advance Payments
****************
#. Create the advance payment Invoice and apply it’s related payment. 
#. Create the final invoice without considering the advance payment. 
#. Create a credit note for the Final invoice with the advance payment amount. 
#. Reconcile the Credit note with the final invoice. 
#. The remaining balance on the final invoice should be paid with a regular payment transaction. 


Credit Notes
------------
When a correction or refund is needed over a validated invoice, a credit note must be generated, 
for this just click on the button “Add Credit Note”, a part of the Peruvian localization you need 
to prove a Credit Reason selecting one of the options in the list.

.. image:: media/peru_24_credit_note.png
   :align: center
   :alt: Credit Note

.. tip::
   When creating your first credit Note, select the Credit Method: Partial Refund, this allows you 
   to define the credit note sequence. 
   
By default the Credit Note is set in the document type:

.. image:: media/peru_25_credit_note_document.png
   :align: center
   :alt: Credit Note document type

To finish the workflow please follow the instructions on 
`this section <https://www.odoo.com/documentation/user/14.0/accounting/receivables/customer_invoices/credit_notes.html>`_.

.. note::
   The EDI workflow for the SUNAT in the same way as the invoices. 


Debit Notes
------------
As part of the Preuvian localization, besides creating credit notes from an existing document 
you can also create debit Notes. For this just use the button “Add Debit Note”.

By default the Debit Note is set in the document type.