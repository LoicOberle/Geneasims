#    Copyright 2020 June Hanabi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import sims4.commands
import services
from sims.sim_info_types import Gender, Age, SpeciesExtended, Species
import os
# This is just a Hello World script, you can play around with it, do a test compile/decompile/debug, or just delete it
# and start from scratch. The world is yours.


@sims4.commands.Command('export', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    #hutput("Pog")
    client = services.client_manager().get_first_client()
    sim_info = client.active_sim.sim_info
    full_name = sim_info.first_name + " " + sim_info.last_name 
    output(full_name)

    output('Your town\'s population is {}'.format(len(services.sim_info_manager().get_all())))
    sims=services.sim_info_manager().get_all()
        
    #with open('C:/Users/Public/test.txt', 'w') as f:
    with open('../../test.txt', 'w') as f:
        for sim in sims:
            sim_info = sim.sim_info
            full_name = sim_info.first_name + " " + sim_info.last_name 
            #output(full_name)
            f.write(full_name+"\n")
            parents=tuple(sim_info.genealogy.get_parent_sim_infos_gen())
            parentStr=""
            for index,parent in enumerate(parents):
                parentStr=parentStr+f'Parent {index+1}'+getFullName(parent)+"\n"
            res=f''' 
                Id: {sim_info.id }
                Prenom: {sim_info.first_name}
                Nom: {sim_info.last_name}
                Genre: {sim_info.gender}
                Age: {sim_info.age}
                Peau: {sim_info.skin_tone}
                Physique: {sim_info.physique}
                World: {sim_info.world_id}
                Espèce??: {SpeciesExtended.get_animation_species_param(sim_info.species)}
                Parent: {parents}
                {parentStr}
                '''
            output(res)
            f.write(res+"\n") 
        output(f"file written ({len(sims)} sims)")
        output(os.getcwd())

# ParentA: {getFullName(findParent(parents[0]))}
#                 ParenB: {getFullName(findParent(parents[1]))}


def getFullName(sim):
    if(sim is not None):
        return sim.sim_info.first_name+" "+sim.sim_info.last_name 


