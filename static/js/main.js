$(function(){
    $(".tab_area li").click(function(){
        var tabbody = $(".panel_area li")
        var idx = tablist.index($(this))
        tablist.removeClass("active").eq(idx).addClass("active")
        tabbody.removeClass("active").eq(idx).addClass("active")
    })


    $("modal_open").click(function(){
        // モーダルウィンドウの黒背景のタグ挿入
        $("body").append('<div class="modal_bg"></div>')
        // 画面中央を算出
        modalResize()

        // モーダルウィンドウ出現
        $(".modal_bg, .modal_window").fadeIn("slow")
        // 閉じる処理
        $(".modal_bg").click(function(){
            $(".modal_bg, .modal_window").fadeOut("slow", function(){
                // 挿入したタグも一緒に消す
                $(".modal_bg").remove()
            })
        })


        //画面中央を算出する処理
        $(window).resize(modalResize)
        function modalResize(){
            var w = $(window).width()
            var h = $(window).height()
            var modalW = $(".modal_window").outerWidth()
            var modalH = $(".modal_window").outerHeight()

            $(".modal_window").css({
                "left": ((w-modalW)/2) + "px",
                "top": ((h-modalH)/2) + "px"
            })
        }
    })
})