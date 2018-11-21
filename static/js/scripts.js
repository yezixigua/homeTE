// 在页面加载完后

var log = function() {
    console.log.apply(console, arguments)
}


jQuery(document).ready(function() {

    /*
        Fullscreen background
    */
	// 暂时没看懂，动态图？
    $.backstretch("img/backgrounds/1.jpg");

    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });

    /*
        Form
    */
    $('.registration-form fieldset:first-child').fadeIn('slow');

    $('.registration-form input[type="text"], .registration-form input[type="password"], .registration-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });

    // next step
    $('.registration-form .btn-next').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;

    	parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			$(this).addClass('input-error');
    			next_step = false;
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});

    	if( next_step ) {
    		parent_fieldset.fadeOut(400, function() {
	    		$(this).next().fadeIn();
	    	});
    	}

    });

    // previous step
    $('.registration-form .btn-previous').on('click', function() {
    	$(this).parents('fieldset').fadeOut(400, function() {
    		$(this).prev().fadeIn();
    	});
    });

//    // submit
//    // 在输入为空的时候改为输入错误class
//    $('.registration-form').on('submit', function(e) {
//        log('已点击')
//    	$(this).find('input[type="text"], input[type="password"]').each(function() {
//    		if( $(this).val() == "" ) {
//    			e.preventDefault();
//    			$(this).addClass('input-error');
//    			log('输入错误')
//    		}
//    		else {
//    			$(this).removeClass('input-error');
//    			log('输入正确')
//
//    		}
//    	});
//
//    });


});
