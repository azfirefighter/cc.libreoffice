import os

class LicenseChooserDialog():
    """Creates a new instance of LicenseChooserDialog
    """

    #TODO: add the global Constants support
    
    #Constants
    #BTN_CC = "btnCC"
    
    def __init__(self, ccLoAddin, ctx):
        """
        
        Arguments:
        - `ccLoAddin`:
        - `ctx`:
        """
        self._ccLoAddin = ccLoAddin
        self.m_xContext = ctx
        
        # get the service manager from the component context
        self.xMultiComponentFactory = self.m_xContext.getServiceManager()

    # The CoreReflection object. 
    def __createUnoStruct(self, cTypeName):
        """Create a UNO struct and return it. 
        
        Arguments:
        - `cTypeName`:
        """
        
        self.xMultiComponentFactory = self.m_xContext.getServiceManager()
       
       
       
        oCoreReflection=self.xMultiComponentFactory.createInstance("com.sun.star.reflection.CoreReflection")
        
        oXIdlClass = oCoreReflection.forName( cTypeName ) 
        oReturnValue, oStruct = oXIdlClass.createObject( None ) 
        return oStruct 

    def __makeRectangle(self, nX, nY, nWidth, nHeight ): 
        """Create a com.sun.star.awt.Rectangle struct.""" 
        
        oRect = self.__createUnoStruct( "com.sun.star.awt.Rectangle" ) 
        
        oRect.X = nX 
        oRect.Y = nY 
        oRect.Width = nWidth 
        oRect.Height = nHeight 
        return oRect
    
    def __createAWTControl(self, xpsProperties, ctrlName,ctrlCaption, posSize, step):
        """Add AWT control components to the dialog.
        
        Arguments:
        - `self`:
        - `xpsProperties`:XPropertySet
        - `ctrlName`:String
        - `ctrlCaption`:String
        - `ctrlName`:String
        - `posSize`:Rectangle - https://gist.github.com/990143
        - `step`:integer
        """
    
        #throw the exceptions
        try:
            xpsProperties.setPropertyValue("PositionX",  posSize.X)
            xpsProperties.setPropertyValue("PositionY",  posSize.Y)
            xpsProperties.setPropertyValue("Width",  posSize.Width)
            xpsProperties.setPropertyValue("Height",  posSize.Height)
            xpsProperties.setPropertyValue("Name", ctrlName)
            xpsProperties.setPropertyValue("Step", step)

            if ctrlCaption is not None:
                xpsProperties.setPropertyValue("Label", ctrlCaption)

            
                
            if ( not self.dlgLicenseSelector.hasByName(ctrlName)):
                self.dlgLicenseSelector.insertByName(ctrlName,xpsProperties)
                
            return xpsProperties
            
        except Exception, ex:
            print "Exception in LicenseChooserDialog.__createAWTControl: "
            print ex
            print type(ex)
            raise ex

    def __crateCC0LicenseTab(self):
        
        ## TODO: move all the Constants near to the top of the class
        LBL_INSTRUCTIONS_CC0 = "lblInstructionsCC0"
        CHK_WAIVE = "chkWaive"
        TXT_LEGAL_CODE_CC0 = "txtLegalCodeCC0"
        CHK_YES_CC0 = "chkYesCC0"
        CMB_TERRITORY = "cmbTerritory"
        
        try:
            
            lblWarning = self.dlgLicenseSelector.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

            ##TODO: add the Java.util support to the following line
            xpsLblWarning = self.__createAWTControl(lblWarning, LBL_INSTRUCTIONS_CC0,"Are you certain you wish to waive all rights to your work? "
                                + "Once these rights are waived, you cannot reclaim them."+ "\n\nIn particular, if you are an artist or author who depends "
                + "upon copyright for your income, "
                + "Creative Commons does not recommend that you use this tool."
                + "\n\nIf you don't own the rights to this work, then do not use CC0. "
                + "\nIf you believe that nobody owns rights to the work, then the "
                + "Public Domain Certification may be what you're looking for.",
                self.__makeRectangle(10, 25, 195, 80), 2)

            xpsLblWarning.setPropertyValue("MultiLine", True)
            fontDes =  xpsLblWarning.getPropertyValue("FontDescriptor")
            fontDes.Weight = 150
            xpsLblWarning.setPropertyValue("FontDescriptor", fontDes)

            chkWaive = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlCheckBoxModel")

            ##TODO:Add java.util support to the following line
            xpsChkWaive = self.__createAWTControl(chkWaive, CHK_WAIVE,
                                "I hereby waive all copyright and related or neighboring rights "
                                + "together with all associated claims and causes of action with "
                                + "respect to this work to the extent possible under the law.",
                                self.__makeRectangle(10, 110, 190, 30), 2)
            

            xpsChkWaive.setPropertyValue("MultiLine", True)

            
            ##Legal code
            path=os.path.join(os.path.dirname(__file__), '../../../license/legalcodes/cc0')
            f=open(path,'r')
            cc0LegalCode=f.read()

            txtDeed = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlEditModel")
            xpsTxtDeed = self.__createAWTControl(txtDeed, TXT_LEGAL_CODE_CC0, None,
                self.__makeRectangle(10, 145, 190, 60), 2)
            xpsTxtDeed.setPropertyValue("MultiLine", True)
            xpsTxtDeed.setPropertyValue("ReadOnly", True)
            xpsTxtDeed.setPropertyValue("VScroll", True)
            xpsTxtDeed.setPropertyValue("Text", cc0LegalCode)


            chkYes = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlCheckBoxModel")
            ##TODO:Add java.util support to the following line
            xpsChkYes = self.__createAWTControl(chkYes, CHK_YES_CC0,
                    "I have read and understand the terms and intended legal effect of CC0, "
                    + "and hereby voluntarily elect to apply it to this work.",
                    self.__makeRectangle(10, 210, 190, 20), 2)
            xpsChkYes.setPropertyValue("MultiLine", True)

            ##Territory
            lblJurisdictionList = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlFixedTextModel")
            xpsLblJurisdictionList = self.__createAWTControl(lblJurisdictionList, "lbltrritory",
                "Territory", self.__makeRectangle(10, 230, 45, 15), 2)

            #TODO: This list currently contains nothing. Add items to the list
            cmbTerritoryList = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlListBoxModel")
            xPSetList = self.__createAWTControl(cmbTerritoryList, CMB_TERRITORY,
                None, self.__makeRectangle(55, 230, 120, 12), 2)
            xPSetList.setPropertyValue("Dropdown", True)
            xPSetList.setPropertyValue("MultiSelection", False)
            
        except Exception,ex:
            print 'Exception in LicenseChooserDialog.__crateCC0LicenseTab'
            print type(ex)
            print ex
            raise ex


    #TODO: Method is not fully implemented.
    def __createCCLicenseTab(self, ):
        """
        """

        ## TODO: move all the Constants near to the top of the class
        LBL_SELECTED_LICENSE_LABEL = "lblSelectedLicense_lbl"
        LBL_SELECTED_LICENSE = "lblSelectedLicense"
        
        try:
            #create the current license information
            lblSelectedLicenseLabel = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlFixedTextModel")
            self.__createAWTControl(lblSelectedLicenseLabel, LBL_SELECTED_LICENSE_LABEL,
                "Selected License:", self.__makeRectangle(10, 20, 50, 15), 1)
            lblSelectedLicense = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlFixedTextModel")
            xpsSelectedLicense = self.__createAWTControl(lblSelectedLicense, LBL_SELECTED_LICENSE,
                None, self.__makeRectangle(60, 20, 145, 30), 1)

            
        except Exception,ex:
            print 'Exception in LicenseChooserDialog.__createCCLicenseTab'
            print type(ex)
            print ex
            raise ex
        


    def showDialog(self):
        """Shows the LicenseChooserDialog 
        
        Arguments:
        - `self`:
        """
       

        #Constants
        BTN_CC = "btnCC"
        BTN_CC0 = "btnCC0"
        BTN_PUBLICDOMAIN = "btnPublicdomain"
        BTN_FAQ = "faqbt"
        faqButtonLabel = "FAQ"
        finishButtonLabel = "OK"
        BTN_OK = "finishbt"
        BTN_CANCEL = "cancelbt"
        cancelButtonLabel = "Cancel"
       
        try:

            #set to modify the global copies of variables
            #global BTN_CC
      
            # create the dialog model and set the properties
            self.dlgLicenseSelector = self.xMultiComponentFactory.createInstanceWithContext(
                "com.sun.star.awt.UnoControlDialogModel", self.m_xContext)


            ###
            #The following part was changed from the origianl code
            ###
            
            #rect=self.__makeRectangle(100, 80, 210, 275)
      
            self.dlgLicenseSelector.Width=210
            self.dlgLicenseSelector.Height=275
            self.dlgLicenseSelector.PositionX=100
            self.dlgLicenseSelector.PositionY=80
            self.dlgLicenseSelector.Title="Sharing & Reuse Permissions"
      

            ##--due to the following commment the following code in __createAWTControl is not run

            ##if ( not self.dlgLicenseSelector.hasByName(ctrlName)):
            ##    self.dlgLicenseSelector.insertByName(ctrlName,xpsProperties)

            
            #xPSetDialog=self.__createAWTControl(self.dlgLicenseSelector, "cc", None,rect,1)
            #xPSetDialog.setPropertyValue("Title", "Sharing & Reuse Permissions")

            #--
            ###
            ###
            
            ###Tabs
            ##CC
            ccButton = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlButtonModel")

           
           
            
            xPSetCCButton = self.__createAWTControl(ccButton, BTN_CC,
                None, self.__makeRectangle(4, 3, 70, 12), 0)

            xPSetCCButton.setPropertyValue("DefaultButton", True)
            
            #TODO: The next line needs localization support. See original code
            #for more details.
           
            xPSetCCButton.setPropertyValue("Label", "Creative_Commons")
            xPSetCCButton.setPropertyValue("Toggle", True)

            fontDes = xPSetCCButton.getPropertyValue("FontDescriptor")
            fontDes.Weight = 150
            xPSetCCButton.setPropertyValue("FontDescriptor", fontDes)
            #TODO: Original code had (short)1
            xPSetCCButton.setPropertyValue("State", 1)

            ##CC0

            cc0Button = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlButtonModel")
            xPSetCC0Button = self.__createAWTControl(cc0Button, BTN_CC0,
                None, self.__makeRectangle(73, 3, 20, 12), 0)
            xPSetCC0Button.setPropertyValue("DefaultButton", True)
            xPSetCC0Button.setPropertyValue("Label", "CC0")
            xPSetCC0Button.setPropertyValue("Toggle", True)
            fontDes = xPSetCC0Button.getPropertyValue("FontDescriptor")
            fontDes.Weight = 75
            xPSetCC0Button.setPropertyValue("FontDescriptor", fontDes)
            #TODO: Original code had (short)0
            xPSetCC0Button.setPropertyValue("State", 0)
            
            ##PD

            pdButton = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlButtonModel")
            xPSetPDButton = self.__createAWTControl(pdButton, BTN_PUBLICDOMAIN,
                None,self.__makeRectangle(92, 3, 60, 12), 0)
            xPSetPDButton.setPropertyValue("DefaultButton", True)
            #TODO: The next line needs localization support.
            xPSetPDButton.setPropertyValue("Label","Public Domain")
            xPSetPDButton.setPropertyValue("Toggle", True)
            fontDes = xPSetPDButton.getPropertyValue("FontDescriptor")
            fontDes.Weight = 75
            xPSetPDButton.setPropertyValue("FontDescriptor", fontDes)
            #TODO: Original code had (short)0
            xPSetPDButton.setPropertyValue("State", 0)

            ##Creates the outer frame like box of the window
            oGBResults = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlGroupBoxModel")
            xpsBox =self.__createAWTControl(
                oGBResults, "box", None, self.__makeRectangle(2, 15, 206, 243), 0)

            ##Create Tabs
            self.__crateCC0LicenseTab()
            self.__createCCLicenseTab()
            print 'passed'

            ##create the button model - FAQ and set the properties
            faqButton = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlButtonModel")
            xPSetFaqButton = self.__createAWTControl(faqButton, BTN_FAQ,
                None, self.__makeRectangle(70, 260, 40, 14), 0)
            xPSetFaqButton.setPropertyValue("DefaultButton", True)
            xPSetFaqButton.setPropertyValue("Label", faqButtonLabel)

            ##create the button model - OK and set the properties
            finishButton = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlButtonModel")
            xPSetFinishButton = self.__createAWTControl(finishButton, BTN_OK,
                None, self.__makeRectangle(115, 260, 40, 14), 0)
            xPSetFinishButton.setPropertyValue("DefaultButton", True)
            xPSetFinishButton.setPropertyValue("Label", finishButtonLabel)

            ## create the button model - Cancel and set the properties
            cancelButton = self.dlgLicenseSelector.createInstance(
                "com.sun.star.awt.UnoControlButtonModel")
            xPSetCancelButton = self.__createAWTControl(cancelButton, BTN_CANCEL,
                None, self.__makeRectangle(160, 260, 40, 14), 0)
            xPSetCancelButton.setPropertyValue("Name", BTN_CANCEL)
            xPSetCancelButton.setPropertyValue("Label", cancelButtonLabel)
            
            ##create the dialog control and set the model
            dialog = self.xMultiComponentFactory.createInstanceWithContext(
                "com.sun.star.awt.UnoControlDialog", self.m_xContext)
            # xControl = dialog
            #xControlModel =  dlgLicenseSelector
            #xControlCont=dialog
            dialog.setModel(self.dlgLicenseSelector)

            ##add an action listener to the Previous button control

            ##add Unported, which isn't actually a jurisdiction'

            ##add a bogus place-holder for Unported in the JurisdictionList to
            ##ensure indices match up when determining the item selectedJurisdiction

            ##Pre-select Unported

            ##listen for license selection changes

            ##add an action listeners to buttons

            ##Set the initial license

            ##create a peer

            
            ##execute the dialog
            dialog.setVisible(True)
            dialog.execute()
            

            ##dispose the dialog
            #dialog.dispose()
            
            
        except Exception,ex:
            print "Exception in LicenseChooserDialog.showDialog:"
            print ex

            #TODO: match the raising exception with the origianl source
            raise ex
