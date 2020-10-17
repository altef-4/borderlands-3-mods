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
from bl3hotfixmod.bl3hotfixmod import Mod
from random import randrange
import math
mod = Mod('all_easy_mayhem2_modifiers.txt',
        'all easy mayhem2 modifiers',
        'altef_4',
        [],
        lic=Mod.CC_BY_SA_40,
        )
x = 0
m2_easy_mod = "MayhemModifierSlotDataAsset'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_EAsy.ModSet_Mayhem2_Easy'"
for i in [
    "({},{})".format(m2_easy_mod,m2_easy_mod),
    "({},{},{})".format(m2_easy_mod,m2_easy_mod,m2_easy_mod),
    "({},{})".format(m2_easy_mod,m2_easy_mod),
    "({},{},{})".format(m2_easy_mod,m2_easy_mod,m2_easy_mod),
    "({},{},{},{})".format(m2_easy_mod,m2_easy_mod,m2_easy_mod,m2_easy_mod),
    "({},{},{})".format(m2_easy_mod,m2_easy_mod,m2_easy_mod),
    "({},{})".format(m2_easy_mod,m2_easy_mod),
    "({},{},{})".format(m2_easy_mod,m2_easy_mod,m2_easy_mod),
    "({},{},{},{})".format(m2_easy_mod,m2_easy_mod,m2_easy_mod,m2_easy_mod),
]:
    x += 1
    mod.reg_hotfix(Mod.EARLYLEVEL, 'TechSlaughter_P',
        '/Game/PatchDLC/Mayhem2/OverrideModSet_Mayhem2.OverrideModSet_Mayhem2',
        'PerLevelOverrides.PerLevelOverrides[{}].RandomModifierSlotsOverride'.format(x),
        i,"",True)
mod.close()