import streamlit as st
import io, sys, os
import captum

import spacy

import torch

import torch.nn as nn
import torch.nn.functional as F

# import torchtext
# import torchtext.data
# from torchtext.vocab import Vocab

from captum.attr import LayerIntegratedGradients, TokenReferenceBase, visualization

nlp = spacy.load('en')


# Page configuration
st.set_page_config(
    page_title="POC for LISTEN",
    page_icon="🔍",
    layout="wide"
)
# Footer
st.markdown("---\nPowered by Streamlit")
