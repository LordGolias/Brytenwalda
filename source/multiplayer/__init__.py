from . import initialization, scripts, mission_templates, presentations, troops, \
    coop_mission_templates, coop_presentations, coop_scripts, scenes

scripts = initialization.scripts + scripts.scripts + coop_scripts.coop_scripts
mission_templates = mission_templates.mission_templates + coop_mission_templates.coop_mission_templates
presentations = presentations.presentations + coop_presentations.coop_presentations
troops = troops.troops
scenes = scenes.scenes
