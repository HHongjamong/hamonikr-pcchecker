import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class ScrolledWindow(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Hamonikr PC Checker - 개인 정보 보호")
        self.set_default_size(500,600)
        self.connect("destroy", Gtk.main_quit)

        scrolledwindow = Gtk.ScrolledWindow()
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box_outer.pack_start(scrolledwindow, 1,1,0)
        self.add(box_outer)


        #privacy gui - after search
        self.box_privacy = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        listbox_id = Gtk.ListBox()
        listbox_pn = Gtk.ListBox()
        listbox_ad = Gtk.ListBox()
        listbox_cd = Gtk.ListBox()
        self.id_check = Gtk.CheckButton()
        self.pn_check = Gtk.CheckButton()
        self.ad_check = Gtk.CheckButton()
        self.cd_check = Gtk.CheckButton()
        self.all_result = []
        self.all_checklist = []

        def set_search(category):
            num = 0
            result = []
            with open('/usr/bin/result'+str(category)+'.txt','r') as resfile:
                lines = resfile.readlines()
                if lines != '':
                    num = lines[0].strip()
                    for i in range(len(lines)-1):
                        if lines[i+1] != '':
                            result.append(lines[i+1].strip())
                else:
                    print('result'+str(category)+'.txt file empty')

            if category == 0:
                expand = Gtk.Expander(label="주민번호로 추정되는 데이터 "+str(num)+"건")
                listbox = listbox_id
                category_check = self.id_check
            elif category == 1:
                expand = Gtk.Expander(label="전화번호로 추정되는 데이터 "+str(num)+"건")
                listbox = listbox_pn
                category_check = self.pn_check
            elif category == 2:
                expand = Gtk.Expander(label="주소로 추정되는 데이터 "+str(num)+"건")
                listbox = listbox_ad
                category_check = self.ad_check
            elif category == 3:
                expand = Gtk.Expander(label="카드번호로 추정되는 데이터 "+str(num)+"건")
                listbox = listbox_cd
                category_check = self.cd_check

            expand.set_expanded(True)
            category_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            checklist = []
            checklist.append(category_check)
            category_box.pack_start(category_check, False, False, 5)
            category_box.pack_start(expand, 0, 0, 0)
            self.box_privacy.pack_start(category_box, 0, 0, 0)
            for file in result:
                if file!="":
                    filepath = file.split(":")[0]
                    search_text = file.split(":")[1]
                    filename = filepath.split("/")[-1]
                    box = Gtk.Box()
                    check = Gtk.CheckButton()
                    checklist.append(check)
                    box.pack_start(check, False, False, 0)
                    filelink = "file://" + filepath
                    btn_file = Gtk.LinkButton(uri=filelink, label=filename)
                    box.pack_start(btn_file, False, False, 0)
                    search_text = Gtk.Label(label=search_text)
                    box.pack_start(search_text, False, False, 5)
                    listbox.add(box)
            expand.add(listbox)
            category_check.connect("toggled",self.on_check_toggled, category_check, checklist)
            self.all_result.append(result)
            self.all_checklist.append(checklist)

        
        # category : id
        set_search(0)
        # category : phone num
        set_search(1)
        # category : address
        set_search(2)
        # category : card num
        set_search(3)
        
        allcheck_btn = Gtk.CheckButton(label="전체선택")
        allcheck_btn.connect("clicked", self.fnt_allcheck, allcheck_btn)
        rm_btn = Gtk.Button(label="일괄 삭제")
        rm_btn.connect("clicked", self.fnt_pirm, self.all_result, self.all_checklist)

        self.privacy_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.privacy_box.pack_start(allcheck_btn, 0, 0, 0)
        self.privacy_box.pack_start(self.box_privacy, 0, 0, 0)
        self.privacy_box.pack_start(rm_btn, 0, 0, 0)

        scrolledwindow.add(self.privacy_box)
        

    def fnt_allcheck(self,widget, allcheck_btn):
        if allcheck_btn.get_active():
            self.id_check.set_active(True)
            self.pn_check.set_active(True)
            self.ad_check.set_active(True)
            self.cd_check.set_active(True)
        else:
            self.id_check.set_active(False)
            self.pn_check.set_active(False)
            self.ad_check.set_active(False)
            self.cd_check.set_active(False)

    def on_check_toggled(self, widget, category_check, checklist):
        if category_check.get_active():
            for check in checklist:
                check.set_active(True)
        else:
            for check in checklist:
                check.set_active(False)

    def fnt_pirm(self, widget, result, checklist):
        for j in range(4):
            i = 0
            for check in checklist[j]:
                if check.get_active():
                    filepath = result[j][i-1].split(":")[0]
                    searched = result[j][i-1].split(":")[1]
                    print('path:',filepath, "   searched:",searched)

                    if filepath.endswith('.hwp'):
                        dialog = Gtk.MessageDialog(
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.OK,
                            text="hwp 형식 파일은 수정할 수 없습니다.",)
                        dialog.run()
                        dialog.destroy()
                    elif filepath.endswith('.pdf'):
                        dialog = Gtk.MessageDialog(
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.OK,
                            text="pdf 형식 파일은 수정할 수 없습니다.",)
                        dialog.run()
                        dialog.destroy()
                    elif filepath.endswith('.odt'):
                        dialog = Gtk.MessageDialog(
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.OK,
                            text="odt 형식 파일은 수정할 수 없습니다.",)
                        dialog.run()
                        dialog.destroy()
                    else:
                        subprocess.run("sudo sed -i 's/"+searched+"//' "+filepath, shell=True)
                i += 1

win = ScrolledWindow()
win.show_all()
Gtk.main()