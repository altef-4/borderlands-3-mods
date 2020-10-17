#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

from bl3hotfixmod.bl3hotfixmod import Mod, BVC

mod = Mod('guardians_health_scalling.txt',
        'restore guardians health scaling',
        'altef_4',
        [
            "restore guardians health scaling",
        ],
        lic=Mod.CC_BY_SA_40,
        )

mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")

mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_88.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
        "10")


# Should maybe add that into our Bloody Harvest enabling thing
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_90.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")

mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_90.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_90.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_90.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_90.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_90.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
        "10")


# Should maybe add that into our Bloody Harvest enabling thing
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_91.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")

mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_91.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_91.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_91.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_91.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_91.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
        "10")


# Should maybe add that into our Bloody Harvest enabling thing
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_89.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")

mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_89.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_89.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_89.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'NumActorsParam.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_89.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_89.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
        "10")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_71.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add1in2PlayerAnd2In4Player.PCF_Add1in2PlayerAnd2In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_71.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter',
        'Waves.Waves[1].Advancement.Percent',
        "0.2")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_100.SpawnerComponent.SpawnerStyle_Encounter_0',
        'Waves.Waves[0].Advancement.Percent',
        "0.3")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_99.SpawnerComponent.SpawnerStyle_Encounter_1.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_100.SpawnerComponent.SpawnerStyle_Encounter_0.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_96.SpawnerComponent.SpawnerStyle_Encounter_3.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_96.SpawnerComponent.SpawnerStyle_Encounter_3',
        'Waves.Waves[0].Advancement.Percent',
        "0.3")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_97.SpawnerComponent.SpawnerStyle_Encounter_2.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_98.SpawnerComponent.SpawnerStyle_Encounter_0.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueAttribute',
        "")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_95.SpawnerComponent.SpawnerStyle_Encounter_2.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_94.SpawnerComponent.SpawnerStyle_Encounter_1.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_94.SpawnerComponent.SpawnerStyle_Encounter_1',
        'Waves.Waves[0].Advancement.Percent',
        "0.3")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_92.SpawnerComponent.SpawnerStyle_Encounter_0.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_92.SpawnerComponent.SpawnerStyle_Encounter_0',
        'Waves.Waves[0].Advancement.Percent',
        "0.3")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_93.SpawnerComponent.SpawnerStyle_Encounter_1.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_3.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_3.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_62.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_62.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_14.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_14.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_36.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_36.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_21.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_21.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_32.SpawnerComponent.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_32.SpawnerComponent.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_48.SpawnerComponent.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_48.SpawnerComponent.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")



mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_49.SpawnerComponent.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenPassive.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")


mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
		'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_49.SpawnerComponent.SpawnerStyle_Den_0',
        'MaxAliveActorsWhenThreatened.AttributeInitializationData.AttributeInitializer',
        "BlueprintGeneratedClass'/Game/GameData/Balance/PlayerCountFormulas/PCF_Add2In2PlayerAnd3In4Player.PCF_Add2In2PlayerAnd3In4Player_C'")

#health scalling
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_FlyerTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "10")
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_HopperTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "15")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "30")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "20")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "8")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "20")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "8")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "12")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "6")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "18")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "16")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "24")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "12")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "25")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "25")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianReaperTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
        "25")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "20")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "8")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "10")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSpectreTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "8")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "12")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianSeraTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "6")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "18")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianHeraldTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "16")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_01_Primary_9_07801BE24749AFC87299AD91E1B82E12',
        "24")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianWraithBadassTD2_LOWXP',
		'/Game/PatchDLC/Takedown2/Enemies/Guardians/_Shared/_Design/Balance/Table_Balance_GuardianTD2.Table_Balance_GuardianTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "12")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_02_Secondary_12_9204082C4992E4200D005C8CBA622E49',
        "5")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_03_Tertiary_16_46D12ED24F464AF5278FAAA2927388E2',
        "3")	
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_04_Quaternary_18_1B102342416A40A8DC163EA34FE48863',
        "3")		
	
mod.reg_hotfix(Mod.CHAR, 'BPChar_Nekrobug_BadassTD2',
		'/Game/PatchDLC/Takedown2/Enemies/Nekrobugs/_Shared/_Design/Balance/Table_Balance_NekrobugTD2.Table_Balance_NekrobugTD2',
        'HealthMultiplier_05_Quinary_20_EC017977469D43823CC907990EEF7113',
        "3")		
mod.close()

