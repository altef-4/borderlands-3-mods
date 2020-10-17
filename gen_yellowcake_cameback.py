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

mod = Mod('yellowcake_cameback.txt',
        'restore yellowcake cameback',
        'altef_4',
        [
            "yellowcake cameback",
        ],
        lic=Mod.CC_BY_SA_40,
        )

mod.reg_hotfix(Mod.PATCH, '',
		'/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Parts/Part_HW_COV_Barrel_ETech_YellowCake.Part_HW_COV_Barrel_ETech_YellowCake',
        'InventoryAttributeEffects.InventoryAttributeEffects[3].ModifierType',
        "Scale")
mod.reg_hotfix(Mod.PATCH, '',
		'/Game/PatchDLC/Event2/Gear/Weapon/DataTable_WeaponBalance_Event2.DataTable_WeaponBalance_Event2',
        'Custom_A_10_6BE78EF448AB3F6F228BC7B266814C86',
        "2")

mod.close()

