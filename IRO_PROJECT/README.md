Akash Guptha Ravva
A20545642

Instructions to run the codes.

1. Web Crawler (Scrapy):
   - Navigate to the directory containing the `web_crawler` code.
   - Run the following command to start the web crawler:

    cd web_crawler 
    scrapy startproject Scrapy.py
    scrapy crawl web_crawler -o output.json 

2. Indexer (TF-IDF Matrix and Cosine Similarity):
   - Ensure that the web crawler has finished crawling and the output JSON file (`output.json`) is generated.
   - Navigate to the directory containing the `Sklearn.py.py` code.
   - Run the following command to create the TF-IDF matrix and cosine similarity calculations:
     python3 Scrapy.py 
   

3. Query Processor (Flask Application):
   - Ensure that the inverted index file (`inverted_index.pkl`) is generated from the indexer.
   - Navigate to the directory containing the Flask application code.
   - Run the following command to start the Flask server:
    export FLASK_APP=Flaasky.py
   flask run  

Once all three commands are running, you can access the Flask application in your web browser at `http://127.0.0.1:5000/` to search for queries and retrieve relevant documents based on the indexed data.