#Author: Ishan Thilina Somasiri
#E-mail: ishan@ishans.info
#Blog: www.blog.ishans.info

from org.creativecommons.libreoffice.program.OOoProgram import OOoProgram

class Calc(OOoProgram):
    """
    """
    
    def __init__(self, component,m_xContext):
        """
        
        Arguments:
        - `component`:XComponent
        - `m_xContext`:XComponentContext
        """
        super(Calc,self).__init__(component,m_xContext)
        
        