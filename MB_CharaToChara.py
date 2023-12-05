#!/usr/bin/env python2.7.6
# coding:utf-8
from pyfbsdk import *
from pyfbsdk_additions import *

global ChList, ChNameList
global SelectChItem, Acter_A, Acter_B, Acter_C, Acter_D
global SceneCharacterList, AddChListA, AddChListB, AddChListC, AddChListD
global ActerItemA, ActerItemB, ActerItemC, ActerItemD

#シーン内のキャラクタをリストし直します
def CollectAllCharacterCallBack(control,event):
    global ChList, ChNameList
    global SceneCharacterList, AddChListA, AddChListB, AddChListC, AddChListD
    global ActerItemA, ActerItemB, ActerItemC, ActerItemD

    SceneCharacterList.Items.removeAll()
    ActerItemA.Items.removeAll()
    ActerItemB.Items.removeAll()
    ActerItemC.Items.removeAll()
    ActerItemD.Items.removeAll()
    AddChListA.Items.removeAll()
    AddChListB.Items.removeAll()
    AddChListC.Items.removeAll()
    AddChListD.Items.removeAll()

    ChList = []
    ChNameList = []
    for i in FBSystem().Scene.Components:
        if i.TypeInfo == 44:
            ChList.append(i)
            ChNameList.append(i.Name)
            SceneCharacterList.Items.append(i.Name)
            ActerItemA.Items.append(i.Name)
            ActerItemB.Items.append(i.Name)

#add acter a が押されたとき、左側のリストで選択したアイテムをacter Aのリストに追加します
def AddActerA_ListCallBack(control,event):
    global SceneCharacterList, AddChListA
    AddList = AddChListA
    AddActerList_ListCallBack(SceneCharacterList,AddList)
#add acter b が押されたとき、左側のリストで選択したアイテムをacter Bのリストに追加します
def AddActerB_ListCallBack(control,event):
    global SceneCharacterList, AddChListB
    AddList = AddChListB
    AddActerList_ListCallBack(SceneCharacterList,AddList)
#add acter c が押されたとき、左側のリストで選択したアイテムをacter Bのリストに追加します
def AddActerC_ListCallBack(control,event):
    global SceneCharacterList, AddChListC
    AddList = AddChListC
    AddActerList_ListCallBack(SceneCharacterList,AddList)
#add acter d が押されたとき、左側のリストで選択したアイテムをacter Bのリストに追加します
def AddActerD_ListCallBack(control,event):
    global SceneCharacterList, AddChListD
    AddList = AddChListC
    AddActerList_ListCallBack(SceneCharacterList,AddList)
#継承したアイテムを継承した怜太ウトナイにリストします
def AddActerList_ListCallBack(SceneCharacterList,AddList):
    #リストを初期化します
    AddList.Items.removeAll()
    #選択されているアイテムを確認してリスト化します
    SelectItems = []
    for i in range(len(SceneCharacterList.Items)):
        if SceneCharacterList.IsSelected(i):
            SelectItems.append(SceneCharacterList.Items[i])
    #リストしたアイテムを左側から削除して、リストAに追記します
    for i in SelectItems:
        print (i)
        AddList.Items.append(i)
        SceneCharacterList.Items.remove(i)

#リストAのアイテムを選択した時、選択したアイテムをリストAからリムーブして、左のリストに返します
def Remove_Ch_A_ListCallBack(control,event):
    global SceneCharacterList, AddChListA
    Remove = AddChListA.Items[control.ItemIndex]
    RemoveList = AddChListA
    RemoveItems_ListCallBack(SceneCharacterList,RemoveList,Remove)

#リストBのアイテムを選択した時、選択したアイテムをリストAからリムーブして、左のリストに返します
def Remove_Ch_B_ListCallBack(control,event):
    global SceneCharacterList, AddChListB
    Remove = AddChListB.Items[control.ItemIndex]
    RemoveList = AddChListB
    RemoveItems_ListCallBack(SceneCharacterList,RemoveList,Remove)

#リストCのアイテムを選択した時、選択したアイテムをリストAからリムーブして、左のリストに返します
def Remove_Ch_C_ListCallBack(control,event):
    global SceneCharacterList, AddChListC
    Remove = AddChListC.Items[control.ItemIndex]
    RemoveList = AddChListC
    RemoveItems_ListCallBack(SceneCharacterList,RemoveList,Remove)

#リストDのアイテムを選択した時、選択したアイテムをリストAからリムーブして、左のリストに返します
def Remove_Ch_D_ListCallBack(control,event):
    global SceneCharacterList, AddChListD
    Remove = AddChListD.Items[control.ItemIndex]
    RemoveList = AddChListD
    RemoveItems_ListCallBack(SceneCharacterList,RemoveList,Remove)

#継承したアイテムを継承したレイアウトからリムーブします
def RemoveItems_ListCallBack(SceneCharacterList,RemoveList,Remove):
    RemoveList.Items.remove(Remove)
    SceneCharacterList.Items.append(Remove)

#アクタAを設定します
def Set_Acter_A_ListCallBack(control,event):
    global Acter_A
    Acter_A = control.Items[control.ItemIndex]
#アクタBを設定します
def Set_Acter_B_ListCallBack(control,event):
    global Acter_B
    Acter_B = control.Items[control.ItemIndex]
#アクタCを設定します
def Set_Acter_C_ListCallBack(control,event):
    global Acter_C
    Acter_C = control.Items[control.ItemIndex]
#アクタDを設定します
def Set_Acter_D_ListCallBack(control,event):
    global Acter_D
    Acter_D = control.Items[control.ItemIndex]

#リストAを設定します
def Set_Ch_A_ListCallBack(control,event):
    global Acter_A, AddChListA
    ActerItem, AddLits = Acter_A, AddChListA
    Set_Ch_ListCallBack(ActerItem, AddLits)

#リストBを設定します
def Set_Ch_B_ListCallBack(control,event):
    global Acter_B, AddChListB
    ActerItem, AddLits = Acter_B, AddChListB
    Set_Ch_ListCallBack(ActerItem, AddLits)
#リストCを設定します
def Set_Ch_C_ListCallBack(control,event):
    global Acter_C, AddChListC
    ActerItem, AddLits = Acter_C, AddChListC
    Set_Ch_C_ListCallBack(ActerItem, AddLits)
#リストDを設定します
def Set_Ch_D_ListCallBack(control,event):
    global Acter_D, AddChListD
    ActerItem, AddLits = Acter_D, AddChListD
    Set_Ch_ListCallBack(ActerItem, AddLits)

#リストを設定します
def Set_Ch_ListCallBack(ActerItem, AddLits):
    global ChList
    #print Acter_A
    if ActerItem in AddLits.Items:
        print ('ソースのキャラクタとソースによって動かされるキャラクタリストに存在しています')
    else:
        TargetCH = ''
        for i in ChList:
            if ActerItem == i.Name:
                TargetCH = i

        for i in AddLits.Items:
            for m in ChList:
                if i == m.Name:
                    m.InputCharacter = TargetCH
                    m.InputType = FBCharacterInputType.kFBCharacterInputCharacter
                    m.ActiveInput = True

def CustomWindowLayout(CustomWindowMain):
    #グローバル変数レイアウトを設定します
    global SceneCharacterList, AddChListA, AddChListB, AddChListC, AddChListD
    global ActerItemA, ActerItemB, ActerItemC, ActerItemD
    #レギオンを設定します
    x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,'')
    y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,'')
    w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,'')
    h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,'')
    #レギオンをアタッチします
    CustomWindowMain.AddRegion('Main', 'Main', x, y, w, h)
    ##水平レイアウトを作成します
    MainLayout = FBHBoxLayout()
    CustomWindowMain.SetControl('Main', MainLayout)
    ###水平レイアウト内にシーン内キャラクタリスト更新用の垂直レイアウトを作成します
    AllScerneCharaLayout = FBVBoxLayout()
    MainLayout.Add(AllScerneCharaLayout,150)

    ####キャラクタリスト更新用の垂直レイアウト内に、更新用ボタンを設置します
    UpdateButton = FBButton()
    UpdateButton.Caption = 'Update'
    UpdateButton.OnClick.Add(CollectAllCharacterCallBack)
    AllScerneCharaLayout.Add(UpdateButton,50)
    ####更新されたシーン内の全てのキャラクタのリストを書き込みます
    SceneCharacterList = FBList()#SceneCharacterListはglobalな変数です
    SceneCharacterList.Style = FBListStyle.kFBVerticalList
    SceneCharacterList.MultiSelect = True
    #SceneCharacterList.OnChange.Add()
    AllScerneCharaLayout.Add(SceneCharacterList,250)

    ###水平レイアウト内にキャラクタ設定変更用のUIをレイアウトするグリッドレイアウトを作成します
    GridLayout = FBGridLayout()
    GridLayout.SetRowRatio(0, 3.0)

    ####左のリストで選択されたアイテムを下のリストに書き込みます
    Add_A_ChButton = FBButton()
    Add_A_ChButton.Caption = 'Add Acter A'
    Add_A_ChButton.OnClick.Add(AddActerA_ListCallBack)
    GridLayout.Add(Add_A_ChButton, 0, 0, height=30)
    ####アクタAに設定されるキャラクタをリストします
    AddChListA = FBList()#AddChListAはglobal変数です
    AddChListA.Style = FBListStyle.kFBVerticalList
    AddChListA.OnChange.Add(Remove_Ch_A_ListCallBack)
    GridLayout.Add(AddChListA, 1, 0, height=250)
    ####アクタAを設定します
    ActerItemA = FBList()
    ActerItemA.Style = FBListStyle.kFBDropDownList
    ActerItemA.OnChange.Add(Set_Acter_A_ListCallBack)
    GridLayout.Add(ActerItemA, 2, 0, height=25)
    ####グリッドレイアウト内でリストに設定された内容を反映させるボタンを配置します
    Set_A_ChButton = FBButton()
    Set_A_ChButton.Caption = 'Set Acter A'
    Set_A_ChButton.OnClick.Add(Set_Ch_A_ListCallBack)
    GridLayout.Add(Set_A_ChButton, 3, 0, height=30)

    ####左のリストで選択されたアイテムを下のリストに書き込みます
    Add_B_ChButton = FBButton()
    Add_B_ChButton.Caption = 'Add Acter B'
    Add_B_ChButton.OnClick.Add(AddActerB_ListCallBack)
    GridLayout.Add(Add_B_ChButton, 0, 1, height=30)
    ####アクタBに設定されるキャラクタをリストします
    AddChListB = FBList()#AddChListBはglobal変数です
    AddChListB.Style = FBListStyle.kFBVerticalList
    AddChListB.OnChange.Add(Remove_Ch_B_ListCallBack)
    GridLayout.Add(AddChListB, 1, 1, height=250)
    ####アクタBを設定します
    ActerItemB = FBList()
    ActerItemB.Style = FBListStyle.kFBDropDownList
    ActerItemB.OnChange.Add(Set_Acter_B_ListCallBack)
    GridLayout.Add(ActerItemB, 2, 1, height=25)
    ####グリッドレイアウト内でリストに設定された内容を反映させるボタンを配置します
    Set_B_ChButton = FBButton()
    Set_B_ChButton.Caption = 'Set Acter B'
    Set_B_ChButton.OnClick.Add(Set_Ch_B_ListCallBack)
    GridLayout.Add(Set_B_ChButton, 3, 1, height=30)

    ####左のリストで選択されたアイテムを下のリストに書き込みます
    Add_C_ChButton = FBButton()
    Add_C_ChButton.Caption = 'Add Acter C'
    Add_C_ChButton.OnClick.Add(AddActerC_ListCallBack)
    GridLayout.Add(Add_C_ChButton, 0, 2, height=30)
    ####アクタBに設定されるキャラクタをリストします
    AddChListC = FBList()#AddChListBはglobal変数です
    AddChListC.Style = FBListStyle.kFBVerticalList
    AddChListC.OnChange.Add(Remove_Ch_C_ListCallBack)
    GridLayout.Add(AddChListC, 1, 2, height=250)
    ####アクタBを設定します
    ActerItemC = FBList()
    ActerItemC.Style = FBListStyle.kFBDropDownList
    ActerItemC.OnChange.Add(Set_Acter_C_ListCallBack)
    GridLayout.Add(ActerItemC, 2, 2, height=25)
    ####グリッドレイアウト内でリストに設定された内容を反映させるボタンを配置します
    Set_C_ChButton = FBButton()
    Set_C_ChButton.Caption = 'Set Acter C'
    Set_C_ChButton.OnClick.Add(Set_Ch_C_ListCallBack)
    GridLayout.Add(Set_C_ChButton, 3, 2, height=30)

    ####左のリストで選択されたアイテムを下のリストに書き込みます
    Add_D_ChButton = FBButton()
    Add_D_ChButton.Caption = 'Add Acter D'
    Add_D_ChButton.OnClick.Add(AddActerD_ListCallBack)
    GridLayout.Add(Add_D_ChButton, 0, 3, height=30)
    ####アクタBに設定されるキャラクタをリストします
    AddChListD = FBList()#AddChListBはglobal変数です
    AddChListD.Style = FBListStyle.kFBVerticalList
    AddChListD.OnChange.Add(Remove_Ch_D_ListCallBack)
    GridLayout.Add(AddChListD, 1, 3, height=250)
    ####アクタBを設定します
    ActerItemD = FBList()
    ActerItemD.Style = FBListStyle.kFBDropDownList
    ActerItemD.OnChange.Add(Set_Acter_D_ListCallBack)
    GridLayout.Add(ActerItemD, 2, 3, height=25)
    ####グリッドレイアウト内でリストに設定された内容を反映させるボタンを配置します
    Set_D_ChButton = FBButton()
    Set_D_ChButton.Caption = 'Set Acter D'
    Set_D_ChButton.OnClick.Add(Set_Ch_D_ListCallBack)
    GridLayout.Add(Set_D_ChButton, 3, 3, height=30)

    #グリッドレイアウトを設定します
    MainLayout.Add(GridLayout,300)


def CreateTool():
    t = FBCreateUniqueTool("List Example")
    CustomWindowLayout(t)
    ShowTool(t)

CreateTool()