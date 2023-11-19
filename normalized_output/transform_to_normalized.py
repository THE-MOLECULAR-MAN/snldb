#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv


# # Documentation
#
# seasons.csv -- seasons of snl
# episodes.csv -- episodes of snl   Season has_many Episodes
#
# titles.csv -- segments of the show.  Episode has_many Titles. Some are Sketches (have a skid).
# appearances.csv -- actions appearing in titles (aid, tid, capacity-Cast/Guest).  An appearance might involve an impression or a character.
#
# characters.csv -- actors playing characters.  referenced from appearances.csv
#
#
#
# sketches.csv -- sketch titles.  Not clear how this is connected. It is referenced in titles.csv. A sketch is a title.
#
#
# Derived data:
#
# casts.csv -- details about cast members.
#

# In[2]:


input_dir = "../output/"
output_dir = "./"


# In[3]:


raw_seasons = pd.read_csv(input_dir + 'seasons.csv')
raw_episodes = pd.read_csv(input_dir + 'episodes.csv')
raw_titles = pd.read_csv(input_dir + 'titles.csv')
raw_appearances = pd.read_csv(input_dir + 'appearances.csv')
# drop charid, impid.
raw_actors = pd.read_csv(input_dir + 'actors.csv')
# type seems overdetermined?


# In[4]:


raw_appearances


# In[5]:


(
    raw_seasons
    .rename(columns={'sid': 'season_id',
                     'first_epid': 'first_episode_id',
                     'last_epid': 'last_episode_id',
                     'n_episodes': 'num_episode_in_season'})
    .to_csv(output_dir + 'seasons.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
)


# In[6]:


(
    raw_episodes
    .rename(columns={'epid': 'episode_id',
                     'sid': 'season_id',
                     'epno': 'episode_order_in_season',
                     'aired': 'aired_at'
                     })
    .reindex(columns=['episode_id', 'aired_at', 'season_id', 'episode_order_in_season'])
    .to_csv(output_dir + 'episodes.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
)


# In[7]:


(
    raw_titles
    .rename(columns={'epid': 'episode_id',
                     'tid': 'segment_id',
                     'order': 'segment_order_in_episode'
                     }
            )
    .drop(columns=['skid', 'sid'])  # redundent
    .reindex(columns=['segment_id', 'name', 'category', 'episode_id', 'segment_order_in_episode'])
    .to_csv(output_dir + 'segments.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
)


# In[8]:


# actors needed below to change actor_name to actor_id.
actors = \
    (
        raw_actors
        .rename(columns={'aid': 'actor_name'})
        .drop(columns=['url'])
        # new primary key for this table
        .assign(actor_id=lambda df_: np.arange(df_.shape[0]) + 1)
        .reindex(columns=['actor_id', 'actor_name', 'gender'])
    )
actors.to_csv(output_dir + 'actors.csv', index=False,
              quoting=csv.QUOTE_NONNUMERIC)


# In[9]:


(
    raw_appearances
    .rename(columns={'tid': 'segment_id',
                     'aid': 'actor_name',
                     'voice': 'is_voice_role'
                     }
            )
    # redundant or too complicated
    .drop(columns=['sid', 'charid', 'impid', 'epid'])
    # new primary key for this table
    .assign(appearance_id=lambda df_: np.arange(df_.shape[0]) + 1)
    # make the relationship to actors go via actor_id and not actor_name
    .merge(actors, how="left", on='actor_name')
    .drop(columns=['gender', 'actor_name'])
    .reindex(columns=['appearance_id', 'actor_id', 'role', 'capacity', 'is_voice_role', 'segment_id'])
    .to_csv(output_dir + 'appearances.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
)


# In[ ]:
