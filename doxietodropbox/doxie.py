import os
import sys
import ntpath
from os import listdir
from os.path import isfile, join

from base import SingleInstance
import settings


from doxieautomator.doxie import DoxieAutomator

import dropbox


class DoxieToDropbox(SingleInstance):
    
    LOCK_PATH = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "DoxieToDropbox-lock")
    doxie = None
    client = None

    def initialize(self):
        
        self.log(u"Looking for Doxie on %s"%(settings.DOXIE_SERVER))

        self.client = dropbox.Dropbox(settings.DROPBOX_ACCESS_TOKEN)
        self.log(u"Dropbox connection: %s"%(self.client))

        self.doxie = DoxieAutomator()
        self.doxie.bind_to(self.notify_new_file)


        

    def loop(self):
        self.doxie.loop()
        self.check_dir_for_new_files()

    def check_dir_for_new_files(self):
        files = []
        for root, directories, filenames in os.walk(settings.DOXIE_FOLDER):
            for filename in filenames: 
                if not filename.startswith('.'):
                    files.append(os.path.join(root,filename))
        
        self.log("Found %s files in the doxie folder %s"%(len(files), settings.DOXIE_FOLDER))
        for file in files:
            self.upload_file(file)

    def notify_new_file(self, local_filename):
        self.log(u"New file downloaded from Doxie to: %s"%(local_filename))
        self.check_dir_for_new_files()
    
    def upload_file(self, local_filepath):
        self.log(u"Going to upload file %s"%(local_filepath))

        f = open(local_filepath, 'rb')
        filename = ntpath.basename(local_filepath)
        abs_filename = u"/%s"%(filename)
        
        try:
            response = self.client.files_upload(bytes(f.read()), abs_filename)
            if os.path.exists(local_filepath):
                os.remove(local_filepath)
            self.log('File uploaded to dropbox and removed from the local directory')
        except dropbox.exceptions.ApiError as e:
            self.log('Error uploading file to Dropbox API: %s'%e)


