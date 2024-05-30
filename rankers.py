import os
import json
import numpy as np

def get_settings():
    if os.path.isfile("cat/plugins/ccat_reranker/settings.json"):
        with open("cat/plugins/ccat_reranker/settings.json", "r") as json_file:
            settings = json.load(json_file)
    return settings

def recent_ranker(documents):
    """
    Returns document in memory sorted by date from most recent.

    Parameters
    ----------
    documents: List of documents (the episodic working memories)

    Returns
    ----------
    recent_docs: The same list but reordered
    """
    if len(documents) == 1:
        return documents
    
    recent_docs = sorted(documents, key=lambda d: d[0].metadata["when"], reverse=True)
    return recent_docs

def litm(documents):
    """
    Function based on Haystack's LITM ranker:
    https://github.com/deepset-ai/haystack/blob/main/haystack/nodes/ranker/lost_in_the_middle.py

    Lost In The Middle is based on the paper https://arxiv.org/abs/2307.03172
    Check it for mor details.


    Parameters
    ----------
    documents: List of documents (the declarative working memories)

    Returns
    ----------
    litm_docs: The same list but reordered
    """
    if len(documents) == 1:
        return documents
    
    document_index = list(range(len(documents)))
    lost_in_the_middle_indices = [0]

    for doc_idx in document_index[1:]:
        insertion_index = len(lost_in_the_middle_indices) // 2 + len(lost_in_the_middle_indices) % 2
        lost_in_the_middle_indices.insert(insertion_index, doc_idx)
        litm_docs = [documents[idx] for idx in lost_in_the_middle_indices]
    return litm_docs

def filter_ranker(documents, tool_threshold):
    """
    Returns list of tools with a similarity score higher than 0.5.

    Parameters
    ----------
    documents: List of documents (the procedural working memories)

    Returns
    ----------
    filtered: The same list but filtered
    """
    filtered = [d for d in documents if d[1]>tool_threshold]
    return filtered

def sbert_ranker(documents, query, model):
    sentence_combinations = [[query, document[0].page_content] for document in documents]
    scores = model.predict(sentence_combinations)
    ranked_indices = np.argsort(scores)[::-1]
    out_list = [documents[idx] for idx in ranked_indices]
    # I don't change the score in the Documents using the reranker score 
    # because it could be very different than the classical bi-encoder and could create mistakes 
    return out_list
