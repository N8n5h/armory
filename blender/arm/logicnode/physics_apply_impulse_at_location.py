import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ApplyImpulseNodeAtLocation(Node, ArmLogicTreeNode):
    '''Apply impulse at location node'''
    bl_idname = 'LNApplyImpulseNodeAtLocation'
    bl_label = 'Apply Impulse At Location'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketVector', 'Impulse')
        self.inputs.new('NodeSocketVector', 'Location')
        self.outputs.new('ArmNodeSocketAction', 'Out')

add_node(ApplyImpulseNodeAtLocation, category='Physics')