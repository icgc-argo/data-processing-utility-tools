#!/usr/bin/env python3

"""
 Copyright (c) 2019, Ontario Institute for Cancer Research (OICR).
                                                                                                               
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>.

 Author: Junjun Zhang <junjun.zhang@oicr.on.ca>
 """


import os
import sys
import json
import requests
from argparse import ArgumentParser


def main(args):
  with open(args.token_file, 'r') as t:
    token = t.read().strip()

  headers = {
    "Authorization": "Bearer %s" % token,
    "Content-Type": "application/json",
    "Accept": "application/json"
  }

  try:
    res = requests.put("%s/studies/%s/analysis/publish/%s" % (args.song_url, args.study, args.analysis_id),
                        headers=headers)
    res.raise_for_status()
    print(res.status_code)
  except requests.exceptions.HTTPError as err:
    sys.exit("SONG analysis publish failed, HTTPError: %s" % err)
  except requests.exceptions.RequestException as err:
    sys.exit("SONG analysis publish failed, RequestException: %s" % err)

  if res.status_code != 200:
    sys.exit("SONG analysis publish failed HTTP status code not 200: %s" % res)


if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-a", "--analysis-id", dest="analysis_id", required=True)
  parser.add_argument("-p", "--study", dest="study", required=True)
  parser.add_argument("-s", "--song-url", dest="song_url", required=True)
  parser.add_argument("-t", "--token-file", dest="token_file", required=True)
  args = parser.parse_args()

  main(args)
