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
from gen_3000_Char_list import *

rdm = randrange(0, len(loot_base))
full_list = r_gun(0)
for gun in range(len(loot_base)):
    if gun != 0:
        full_list = "{},{}".format(full_list,r_gun(gun))

def mob_held_wpn(mod, bpchar, last_bit):
    mod.reg_hotfix(Mod.CHAR, last_bit,
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
            'PlayThroughs.PlayThroughs[1].EquippedItemPoolCollections.EquippedItemPoolCollections[0].ItemPools',
            "((ItemPool=ItemPoolData'{}',PoolProbability=(BaseValueConstant=1.00000)))".format(loot_pool[1]))

    mod.reg_hotfix(Mod.CHAR, last_bit,
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
            'PlayThroughs.PlayThroughs[1].EquippedItemPoolCollections.EquippedItemPoolCollections[0].ItemPools.ItemPools[0].ItemPool.BalancedItems',
            "({})".format(full_list))


    mod.reg_hotfix(Mod.CHAR, last_bit,
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
            'PlayThroughs.PlayThroughs[1].bOverrideDropOnDeathItemPools',
            "True")

    mod.reg_hotfix(Mod.CHAR, last_bit,
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
            'PlayThroughs.PlayThroughs[1].DropOnDeathItemPools.ItemPools',
            "((ItemPool=ItemPoolData'{}',PoolProbability=(BaseValueConstant=1.00000)))".format(loot_pool[1]))

    mod.reg_hotfix(Mod.CHAR, last_bit,
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
            'BPlayThroughs.PlayThroughs[1].DropOnDeathItemPools.ItemPools.ItemPools[0].ItemPool.BalancedItems',
            "({})".format(full_list))
        
    mod.reg_hotfix(Mod.CHAR, last_bit,
            '{}.{}_C:AIBalanceState_GEN_VARIABLE'.format(bpchar,last_bit),
            'PlayThroughs.PlayThroughs[1].bEquipSingleItemFromCollection',
            "False")