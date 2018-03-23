import sublime
import sublime_plugin


class AwselecttofileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # replace all content by horse using following two lines
        # allcontent = sublime.Region(0, self.view.size())
        # self.view.replace(edit,allcontent,'                               ,|     \n                             //|                              ,|\n                           //,/                             -~ |\n                         // / |                         _-~   /  ,\n                       /\'/ / /                       _-~   _/_-~ |\n                      ( ( / /\'                   _ -~     _-~ ,/\'\n                       \\~\\/\'/|             __--~~__--\\ _-~  _/,\n               ,,)))))));, \\/~-_     __--~~  --~~  __/~  _-~ /\n            __))))))))))))));,>/\\   /        __--~~  \\-~~ _-~\n           -\\(((((\'\'\'\'(((((((( >~\\/     --~~   __--~\' _-~ ~|\n  --==//////((\'\'  .     `)))))), /     ___---~~  ~~\\~~__--~ \n          ))| @    ;-.     (((((/           __--~~~\'~~/\n          ( `|    /  )      )))/      ~~~~~__\\__---~~__--~~--_\n             |   |   |       (/      ---~~~/__-----~~  ,;::\'  \\         ,\n             o_);   ;        /      ----~~/           \\,-~~~\\  |       /|\n                   ;        (      ---~~/         `:::|      |;|      < >\n                  |   _      `----~~~~\'      /      `:|       \\;\\_____// \n            ______/\\/~    |                 /        /         ~------~\n          /~;;.____/;;\'  /          ___----(   `;;;/               \n         / //  _;______;\'------~~~~~    |;;/\\    /          \n        //  | |                        /  |  \\;;,\\              \n       (<_  | ;                      /\',/-----\'  _>\n        \\_| ||_                     //~;~~~~~~~~~ \n            `\\_|                   (,~~ \n                                    \\~\\ \n                                     ~~ \n')


        # self.view.insert(edit, 0, "Hello, World!")
        # (row1, col) = self.view.rowcol(self.view.sel()[0].begin())
        # (row2, col) = self.view.rowcol(self.view.sel()[1].begin())

        # get the selection region and string between the region
        selected_region = sublime.Region(self.view.sel()[0].begin(), self.view.sel()[1].end())

        # get the selection fron begining of line of 1st selection to end of line of 2nd selection 
        selected_region = self.view.full_line(selected_region)
        selection = self.view.substr(selected_region)

        # create new file and switch to it
        new_file = self.view.window().new_file()
        self.focus_view(new_file, selection, edit)

    def focus_view(self, view, text, edit):
        window = view.window()
        window.focus_view(view)
        # window.run_command('focus_neighboring_group')
        # window.focus_view(view)

        # insert the text in new file
        view.insert(edit, 0, text + "\n")
'''
        try:
            from .Edit import Edit as Edit
        except:
            from Edit import Edit as Edit

        with Edit(view) as edit:
            edit.insert(0, text + "\n")
'''

