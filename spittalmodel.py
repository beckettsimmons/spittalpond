import json
from spittalbase import SpittalBase

class SpittalModel(SpittalBase):
    """ Handles everything model related. """

    def create_version(self, version_type, upload_id, pkey,
                       pub_user, module_supplier_id):
        """ Creates a version with the upload and download IDs.

        Keyword arguments:
        version_type -- defines the type of version to upload.
        upload_id -- the id returned from create_file_upload().
        pkey -- UNKONW
        pub_usr -- the public user used to name certain things.
        module_supplier_id -- id of the module that supplies the
                              python and SQL code for this file.
                              See /oasis/django/oasis/app/scripts/Dict
        """
        response = self.do_request(
            self.base_url +
            "/oasis/create" + self.types[version_type] + "/" +
            pub_user + "/" +
            str(module_supplier_id) + "/" +
            str(upload_id) + "/" +
            str(pkey) + "/"
        )
        return response

    def create_model_structures(self, module_supplier_id=1):
        """ Creates supporting module structure from the data_dict. """
        ##### Create the Model Structures ####
        for type_name, type_ in self.data_dict.iteritems():
            splitname = type_name.replace(".", "_").split("_")
            # For dictionary types.
            if splitname[0] == 'dict':
                creation_response = self.create_dict(
                    type_name,
                    type_['upload_id'],
                    type_['download_id'],
                    self.pub_user,
                    module_supplier_id
                )
                type_['id'] = json.loads(creation_response.content)['id']

            elif splitname[0] == 'version':
                # For version types.
                creation_response = self.create_version(
                    type_name,
                    type_['upload_id'],
                    type_['download_id'],
                    "ModelKey", # What is this?!
                    module_supplier_id
                )
                type_['id'] = json.loads(
                    creation_response.content
                )['id']
        print('Finished creating model strutures.')