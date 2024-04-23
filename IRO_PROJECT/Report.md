
Akash Guptha Ravva
A20545642

Abstract:

The project, "Web Document Retrieval and Search System for Presidency University Website," encompasses the development of a web crawler, a search indexer, and a query processor, integrated into a cohesive system. The web crawler, implemented using Scrapy, is designed to crawl web pages from the Presidency University website, starting from a seed URL. The search indexer uses Scikit-Learn's TfidfVectorizer to create a TF-IDF matrix from the extracted textual content. The query processor, built with Flask, provides a user-friendly interface for querying the indexed content, correcting spelling errors, and expanding queries using WordNet.

Overview:

The project implements a web document retrieval and search system specifically tailored for the Presidency University website. It comprises a web crawler that fetches web pages, a search indexer that creates a TF-IDF matrix for document similarity, and a query processor that handles user queries. The system aims to provide efficient and accurate information retrieval from web documents related to Presidency University.

Design:

The system design revolves around three main components: the web crawler, the search indexer, and the query processor.

Web Crawler:

Capabilities: The web crawler is capable of crawling web pages from the Presidency University website, starting from a seed URL. It can limit the number of pages and the depth of crawling.

Interactions: It fetches web pages, extracts content, and follows links within the Presidency University domain.

Integration: Outputs scraped data in JSON format for indexing.

2. Search Indexer:

Capabilities: The search indexer creates a TF-IDF matrix from the extracted document content for similarity calculation.

Interactions: It vectorizes document content, calculates cosine similarity, and stores the TF-IDF matrix and feature names.

Integration: Outputs an inverted index in a pickle file format for querying.

3. Query Processor:

   Capabilities: The query processor validates user queries, corrects spelling errors, expands queries using WordNet, and ranks results by similarity.

   Interactions: It receives user queries, processes them using TF-IDF, and returns relevant document URLs and excerpts.

   Integration: Utilizes the TF-IDF matrix and feature names from the search indexer for processing.

Architecture:

The system architecture is structured around the web crawler, search indexer, and query processor, each fulfilling a specific role:

Web Crawler:

   Software Components: Scrapy Spider, Request Handler, URL Parser.

  Interfaces: Uses Scrapy framework for web crawling, communicates with the search indexer to store scraped data.

   Implementation: Initiates crawling from a seed URL, follows links within the Presidency University domain up to a specified depth, and extracts content.

2. Search Indexer:

   Software Components: TF-IDF Vectorizer, Cosine Similarity Calculator, Inverted Indexer.

   Interfaces: Uses Scikit-Learn for TF-IDF vectorization and cosine similarity calculation, stores inverted index in a pickle file for later use.

   Implementation: Creates a TF-IDF matrix from scraped document content, calculates cosine similarity, and stores the inverted index for querying.

3. Query Processor:
   Software Components: Query Validator, Spelling Corrector, Query Expander.

   Interfaces: Utilizes NLTK for natural language processing tasks, communicates with the search indexer to retrieve relevant documents.

  Implementation: Validates user queries, corrects spelling errors, expands queries, and ranks results based on similarity.

Operation:

To run all three components of the project, follow these steps:

1. Web Crawler (Scrapy):
   - Navigate to the directory containing the `web_crawler` code.
   - Run the following command to start the web crawler:
   
     scrapy crawl web_crawler
    

2. Indexer (TF-IDF Matrix and Cosine Similarity):
   - Ensure that the web crawler has finished crawling and the output JSON file (`output.json`) is generated.
   - Navigate to the directory containing the `create_index.py` code.
   - Run the following command to create the TF-IDF matrix and cosine similarity calculations:
     python create_index.py

3. Query Processor (Flask Application):
   - Ensure that the inverted index file (`inverted_index.pkl`) is generated from the indexer.
   - Navigate to the directory containing the Flask application code.
   - Run the following command to start the Flask server:
     python app.py
   

Once all three components are running, the Flask application can be accessed in a web browser at `http://127.0.0.1:5000/` to search for queries and retrieve relevant documents based on the indexed data.

Conclusion:

The project successfully implemented a web document retrieval and search system tailored for the Presidency University website. It utilized a web crawler to extract data, a
search indexer to create a TF-IDF matrix, and a query processor to handle user queries. The system demonstrated efficient and accurate information retrieval capabilities.

Data Sources:

The data source for this project is the website of Presidency University, available at https://presidencyuniversity.in/. The data was accessed through web crawling using Scrapy, and the extracted content was used for indexing and searching within the project.

Test Cases:

The project can be tested using various scenarios to ensure the correctness and robustness of each component. Test cases should include scenarios such as crawling different websites, handling different page structures, verifying the accuracy of the TF-IDF matrix, and evaluating the search results for different queries. Additionally, performance testing can be conducted to measure the efficiency of the search algorithm and the scalability of the system.

Source Code:

The source code for the project is available and includes comprehensive listings and documentation. The project relies on several open-source libraries, including Scrapy, Scikit-Learn, and Flask, which are essential for its functionality and have been carefully documented for transparency and reproducibility. The source code is organized and documented to facilitate easy understanding and modification by developers.

Bibliography:

Scrapy Documentation: https://docs.scrapy.org/
Flask Documentation: https://flask.palletsprojects.com/
NLTK Documentation: https://www.nltk.org/

This comprehensive report outlines the development and implementation of a web document retrieval and search system specifically designed for the Presidency University website. The system's components, functionalities, and interactions are detailed, providing a clear understanding of its design and operation. Further enhancements and optimizations are suggested to improve the system's performance and user experience.









