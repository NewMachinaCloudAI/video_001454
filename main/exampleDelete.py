import time
from pinecone import Pinecone

pc = Pinecone( api_key="YOUR-API-KEY" )

# Create Index if not already created
if 'my-index' in pc.list_indexes().names():
    pc.delete_index( name='my-index' )
    
    print("Pinecone Index Deleted")
else:
    print("Pinecone Index Had Already been Deleted")
