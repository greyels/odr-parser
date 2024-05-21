import json
from config import config as cfg


class ODRParser:
    def __init__(self):
        self.jds_number = 0
        self._relevant_jds = []

    def find_relevant_jds(self, json_fn, keyword_list, level, no_language):
        with open(json_fn, "r") as odr:
            jds = json.load(odr)
        self.jds_number = len(jds)
        for jd in jds:
            if jd.get("Role Language") and no_language.lower() in jd["Role Language"].lower():
                continue
            if jd.get("Role Career Level To") and jd["Role Career Level To"] == cfg.AL:
                jd["Role Career Level To"] = 1
            if jd.get("Role Career Level From") and jd["Role Career Level From"] == cfg.AL:
                jd["Role Career Level From"] = 1
            if str(level).lower() != "any":
                if level > int(jd["Role Career Level From"]) or level < int(jd["Role Career Level To"]):
                    continue
            for kw in keyword_list:
                if jd.get("Role Description") and kw.lower() in jd["Role Description"].lower() or \
                        jd.get("Role Title") and kw.lower() in jd["Role Title"].lower() or \
                        jd.get("Role Primary Skill") and kw.lower() in jd["Role Primary Skill"].lower() or \
                        jd.get("Role Secondary Skill") and kw.lower() in jd["Role Secondary Skill"].lower() or \
                        jd.get("Role Other Skills") and kw.lower() in jd["Role Other Skills"].lower():
                    self._relevant_jds.append(jd)
                    break

    def print_relevant_jds(self):
        print('========================================================')
        print(f"JDs in total => {self.jds_number}")
        print(f"Relevant JDs found => {len(self._relevant_jds)}")
        for jd in self._relevant_jds:
            if jd.get("Role Primary Skill"):
                jd["Role Primary Skill"] = " ".join(jd["Role Primary Skill"].split())
            if jd.get("Role Secondary Skill"):
                jd["Role Secondary Skill"] = " ".join(jd["Role Secondary Skill"].split())
            if jd.get("Role Other Skills"):
                jd["Role Other Skills"] = " ".join(jd["Role Other Skills"].split())
            if jd.get("Role Language"):
                jd["Role Language"] = " ".join(jd["Role Language"].split())
            print(
                '========================================================',
                jd.get("Role ID"),
                f'"{jd.get("Role Title")}" at "{jd.get("Client")}"',
                f'Role Dates -> {jd.get("Role Start Date")} - {jd.get("Role End Date")}',
                f'Role Career Levels -> {jd.get("Role Career Level From")} - {jd.get("Role Career Level To")}',
                f'Role Work Location -> {jd.get("Role Work Location")}',
                f'Role Language -> {jd.get("Role Language")}',
                f'Role Primary Skill -> {jd.get("Role Primary Skill")}',
                f'Role Secondary Skill -> {jd.get("Role Secondary Skill")}',
                f'Role Other Skills -> {jd.get("Role Other Skills")}',
                f'Role Description -> {jd.get("Role Description")}',
                f'Role Primary Contact -> {jd.get("Role Primary Contact")}',
                '',
                sep='\n'
            )
