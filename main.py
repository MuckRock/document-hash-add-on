"""
This Add-On computes the SHA-1 hash of a document and saves it as a key/value pair on the document. 
"""

from documentcloud.addon import SoftTimeOutAddOn

class Hash(SoftTimeOutAddOn):
    """Creates a hash key equal to the document's file hash"""

    def main(self):
        for document in self.get_documents():
            document.data["hash"] = document.file_hash
            document.save()

if __name__ == "__main__":
    Hash().main()
