"""
This Add-On computes the SHA-1 hash of a document and saves it as a key/value pair on the document. 
"""

from documentcloud.addon import SoftTimeOutAddOn
import hashlib

class Hash(SoftTimeOutAddOn):
    """An example Add-On for DocumentCloud."""

    def main(self):
        for document in self.get_documents():
            hash = hashlib.sha1(document.pdf).hexdigest()
            document.data.update({"hash": hash}) 
            document.save()

if __name__ == "__main__":
    Hash().main()
