import pandas as pd
from binance.client import Client
import ta
import pandas_ta as pda
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored

api_key = 'u0pqjDQJPDv1tAnID2BxmQAaY6Bt1tJjwidR3znag8xiMcKY8fkfwglKu0vfWLoL'
api_secret = 'zJNTsXizKM2lh1R0tDDSNQbvdUuBCfBJFpVDjHeZ6dVNHUNl9JT1P6Ol4ifQ6IQQ'
client = Client(api_key, api_secret)
