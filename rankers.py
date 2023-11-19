import os
import json
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

def filter_ranker(documents):
    """
    Returns list of tools with a similarity score higher than 0.5.

    Parameters
    ----------
    documents: List of documents (the procedural working memories)

    Returns
    ----------
    tools: The same list but reordered
    """