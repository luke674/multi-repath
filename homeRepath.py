import maya.cmds as cmds
import os

def openFileAndRemapRefs():
    multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"

    # Choose file to open
    filename = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2, fileMode=1)

    # Open file with no reference loaded
    cmds.file( filename[0], open=True, force=True );
    
    userDirectory = cmds.workspace(q=True, rd=True)

    # Dir containing the references
    refDir1 = userDirectory+'/assets/characters/cartoony/'
    refDir2 = userDirectory+'/assets/characters/realistic/'
    refDir3 = userDirectory+'/assets/characters/animals/'
    refDir4 = userDirectory+'/assets/'
    refDir5 = userDirectory+'/assets/environments/'
    refDir6 = userDirectory+'/assets/props/'

    # A list of any references found in the scene
    references = cmds.ls(type='reference')

    # For each reference found in scene, load it with the path leading up to it replaced
    for ref in references:
        refFilepath = cmds.referenceQuery(ref, f=True)
        print refFilepath
        refFilename = os.path.basename( refFilepath )
        print refFilename
        if os.path.isfile(refDir1+refFilename):
            rePath = refDir1
            print 'path 1 successfull'
            cmds.file( os.path.join(rePath, refFilename), loadReference=ref, options='v=0;')
        elif os.path.isfile(refDir2+refFilename):
            rePath = refDir2 
            print 'path 2 successfull'
            cmds.file( os.path.join(rePath, refFilename), loadReference=ref, options='v=0;')
        elif os.path.isfile(refDir3+refFilename):
            rePath = refDir3 
            print 'path 3 successfull'
            cmds.file( os.path.join(rePath, refFilename), loadReference=ref, options='v=0;') 
        elif os.path.isfile(refDir4+refFilename):
            rePath = refDir4 
            print 'path 4 successfull'
            cmds.file( os.path.join(rePath, refFilename), loadReference=ref, options='v=0;') 
        elif os.path.isfile(refDir5+refFilename):
            rePath = refDir5 
            print 'path 5 successfull'
            cmds.file( os.path.join(rePath, refFilename), loadReference=ref, options='v=0;') 
        elif os.path.isfile(refDir6+refFilename):
            rePath = refDir6 
            print 'path 6 successfull'
            cmds.file( os.path.join(rePath, refFilename), loadReference=ref, options='v=0;') 
        else : 
            print 'failed to find refference'
            cmds.confirmDialog( title='Refference missing', message='One of your references is not from UAL library. Would you like to continue?', button=['Yes'], defaultButton='Yes', dismissString='No' )
        print 'Reference ' + ref + ' found at: ' + cmds.referenceQuery(ref, f=True)   
        

openFileAndRemapRefs()