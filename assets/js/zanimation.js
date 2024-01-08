(function($) {
	"use strict";

	function getController(el, options){
		var $this 	= $(el),
			controller = $this.data("zanim");
		
		if (options === undefined) { 
			options = {delay: 0, duration: 0.8, ease: 'Expo.easeOut', from:{}, to:{}}; 
		}


		//populating the controller
		controller.delay || (controller.delay = options.delay);
		controller.duration || (controller.duration = options.duration);
		controller.from || (controller.from = options.from);
		controller.to || (controller.to = options.to);
		controller.ease && (controller.to.ease = controller.ease) && controller.to.ease || (controller.to.ease = options.ease);
		
		return controller;
	}



	$.fn.zanimation = function(options) {
		
		var $this = $(this);

		//for Timeline
		if($this.data("zanim-timeline")) {

			var timeline = new TimelineMax();

			$this.find('*[data-zanim]').each(function(){
	        	var controller = getController(this, options);
	        	timeline.fromTo($(this), controller.duration, controller.from, controller.to, controller.delay).pause();
	        });

			return timeline;
		}

		//for single elements outside timeline
		else if(!$this.parents("[data-zanim-timeline]").length){
			var controller = getController(this, options);
			return TweenMax.fromTo($this, controller.duration, controller.from, controller.to).delay(controller.delay).pause();
		}

		return new TimelineMax();

	}

}(jQuery));




// triggering zanimation when the element enters in the view
(function($) {

	function isScrolledIntoView($this){

	    var $elem = $this,
	    	windowHeight = $(window).height(),
	    	elemTop = $elem.offset().top,
	    	elemHeight = $elem.height();
	    	windowScrollTop = $(window).scrollTop();

	    	if(elemTop <= (windowScrollTop + windowHeight) && windowScrollTop <= (elemTop + elemHeight)){
	    		return true;
	    	} 
    		return false;
	}

	function triggerZanimation($this){
		if(isScrolledIntoView($this) && $this.attr('data-zanim-trigger')=='scroll') {
			$this.zanimation(zanimationDefaults).play();
			$this.removeAttr('data-zanim-trigger');
		}
	}


	$(document).ready(function() { 
	//playing zanimation for scroll triggers
		$("*[data-zanim-trigger='scroll']").each(function(){
			var $this = $(this);
			triggerZanimation($this);
			$(window).on('scroll', function(){triggerZanimation($this)});
		});
	});


}(jQuery));