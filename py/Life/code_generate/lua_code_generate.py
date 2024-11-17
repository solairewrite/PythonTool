# Author        : jizhixin
# Date          : 2024-08-04
# Description   : 自动化生成Lua代码

import os
from colorama import init, Fore

material_slots = {
    'Head': 2,
    'Torso': 1,
    'Pelvis': 0,
    'UpperLegs': 6,
    'LowerLegs': 7,
    'Feet': 8,
    'Shoulder_L': 4,
    'UpperArm_L': 3,
    'LowerArm_L': 5,
    'Hand_L': 9,
    'Shoulder_R': 12,
    'UpperArm_R': 11,
    'LowerArm_R': 13,
    'Hand_R': 14,
}


def func1():
    for key, value in material_slots.items():
        info = 'self.{0} = self.Mesh:CreateDynamicMaterialInstance({1})'.format(key, value)
        print(info)


def func2():
    for key in material_slots.keys():
        info = 'self.{0}:SetVectorParameterValue(MaterialParamName_BaseColor, self.DefaultColor)'.format(key)
        print(info)


def func_layer_3(item_dict, color):
    for key, value in item_dict.items():
        info = '''
        local OverlayColor_{0} = UKismetMathLibrary.LinearColorLerp(self.OverlayLayerColor, self.AdditiveAmount_Color,
                self:GetAnimCurveValue('Layering_{1}_Add'))
        local Color_{0} = UKismetMathLibrary.LinearColorLerp(self.BaseLayerColor, OverlayColor_{0},
                self:GetAnimCurveValue('Layering_{1}'))
        self.{0}:SetVectorParameterValue(MaterialParamName_BaseColor, Color_{0})
            '''.format(key, value)
        print(color + info)


def func_layer_2(item_dict, color):
    for key, value in item_dict.items():
        info = '''
        local Color_{0} = UKismetMathLibrary.LinearColorLerp(self.BaseLayerColor, self.AdditiveAmount_Color,
                self:GetAnimCurveValue('Layering_{1}'))
        self.{0}:SetVectorParameterValue(MaterialParamName_BaseColor, Color_{0})
        '''.format(key, value)
        print(color + info)


def func_hand(left_right, color):
    info = '''
    local LayerColor_Hand_{0} = UKismetMathLibrary.LinearColorLerp(Color_LowerArm_{0}, self.Hand_Color,
            self:GetAnimCurveValue('Layering_Hand_{0}'))
    local Color_Hand_{0} = UKismetMathLibrary.LinearColorLerp(LayerColor_Hand_{0}, self.HandIK_Color,
            self:GetAnimCurveValue('Enable_HandIK_{0}'))
    self.Hand_{0}:SetVectorParameterValue(MaterialParamName_BaseColor, Color_Hand_{0})
    '''.format(left_right)
    print(color + info)


def func3():
    layers = {
        'Head': 'Head',
        'Torso': 'Spine',
    }
    func_layer_3(layers, Fore.YELLOW)

    layers = {
        'Pelvis': 'Pelvis',
        'UpperLegs': 'Legs',
        'LowerLegs': 'Legs',
        'Feet': 'Legs',
    }
    func_layer_2(layers, Fore.CYAN)

    for left_right in ['L', 'R']:
        layers.clear()
        layers['Shoulder_' + left_right] = 'Arm_' + left_right
        layers['UpperArm_' + left_right] = 'Arm_' + left_right
        layers['LowerArm_' + left_right] = 'Arm_' + left_right

        func_layer_3(layers, Fore.GREEN)
        func_hand(left_right, Fore.MAGENTA)


def func4():
    items = [
        'Default',
        'Masculine',
        'Feminine',
        'Injured',
        'HandsTied',
        'Rifle',
        'Pistol_1H',
        'Pistol_2H',
        'Bow',
        'Torch',
        'Binoculars',
        'Box',
        'Barrel',
    ]

    for item in items:
        info = '{0} = UEnum.ALS_OverlayState.{0},'.format(item)
        print(info)

    for index, item in enumerate(items):
        info = 'if self.OverlayState == OverlayState.{0} then\n'.format(item)
        if index > 0:
            info = 'else' + info
        if index == len(items) - 1:
            info += '\nend'
        print(Fore.YELLOW + info)


def main():
    # func1()
    # func2()
    # func3()
    func4()


if __name__ == '__main__':
    init(autoreset=True)
    main()
