// Checking Viewport
function isElementInViewport (el) {
	"use strict";
	if (typeof jQuery === "function" && el instanceof jQuery) {
		el = el[0];
	}

	var rect = el.getBoundingClientRect();

	return (
		rect.top >= 0 &&
		rect.left >= 0 &&
		rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /*or $(window).height() */
		rect.right <= (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */
	);
}


// function getZanimController(el, options){
//      var $this       = $(el),
//      controller  = $this.data("zanim");

//      // if($this.parents(".timeline").length) return;
		
//      if (options === undefined) { 
//          options = {delay: 0, duration: 0.8, ease: 'Expo.easeOut', from:{}, to:{}}; 
//      }


//      controller.delay || (controller.delay = options.delay);
//      controller.duration || (controller.duration = options.duration);
		
//      controller.from || (controller.from = options.from);
//      controller.to || (controller.to = options.to);

//      controller.ease && (controller.to.ease = controller.ease) && controller.to.ease || (controller.to.ease = options.ease);
//      // console.log(el); console.log(options); console.log(controller);
//      return controller;
// }




// (function($) {
//  "use strict";
//  $.fn.zanimation = function(options) {
		
//      var $this       = $(this),
//          controller  = $this.data("zanim");

//      if($this.parents(".timeline").length) return;
		
		
//      if (options === undefined) { 
//          options = {delay: 0, duration: 0.8, ease: 'Expo.easeOut', from:{}, to:{}}; 
//      }


//      // controller.delay || (controller.delay = options.delay);
//      // controller.duration || (controller.duration = options.duration);
		
//      // controller.from || (controller.from = options.from);
//      // controller.to || (controller.to = options.to);

//      // controller.ease && (controller.to.ease = controller.ease) && controller.to.ease || (controller.to.ease = options.ease);

		


//      return TweenMax.fromTo($this, controller.duration, controller.from, controller.to).delay(controller.delay);
//  }

// }(jQuery));



// // (function($) {
// //   "use strict";
// //   $.fn.zanimationTimeline = function(options, timeline) {
		
// //       var $this       = $(this),
// //           controller  = $this.data("zanim");

// //       // if($this.parents(".timeline").length) return;
		
		
// //       if (options === undefined) { 
// //           options = {delay: 0, duration: 0.8, ease: 'Expo.easeOut', from:{}, to:{}}; 
// //       }


// //       controller.delay || (controller.delay = options.delay);
// //       controller.duration || (controller.duration = options.duration);
		
// //       controller.from || (controller.from = options.from);
// //       controller.to || (controller.to = options.to);

// //       controller.ease && (controller.to.ease = controller.ease) && controller.to.ease || (controller.to.ease = options.ease);

		


// //       return TweenMax.fromTo($this, controller.duration, controller.from, controller.to).delay(controller.delay);
// //   }

// // }(jQuery));




// // triggering for onscroll animation
// // todo: animation iteration: loop & once
// function zanimationScroll(options){

//  var triggerZanimation = function($this){
//      if(isElementInViewport($this) && $this.attr('data-zanim')) {
//              $this.zanimation(options).play();
//          $this.removeAttr('data-zanim');
//          }
//  }

//  function triggerZanimationTimeline($this, timeline){
//      if(isElementInViewport($this) && $this.attr('data-timeline')) {
//          timeline.play();
//          $this.removeAttr('data-timeline');
//          }
//  }


//     $('*[data-zanim]').each(function(){
//         var $this = $(this);
//         if($this.parents("*[data-timeline]").length) return;

//         if($this.data("zanim").trigger == "scroll"){
//          triggerZanimation($this);
//          $(window).on('scroll', function(){triggerZanimation($this)});
//         }
//     });


//     $('*[data-timeline]').each(function(){
//         var $this = $(this);
//         var timeline = new TimelineMax();

//         $this.find('*[data-zanim]').each(function(){
//          // timeline.fromTo($(this), 1, {opacity: 0, scale: 2}, {opacity: 1, scale: 1, ease: Expo.easeOut}, '-=0.3');
//          var controller = getZanimController(this, options);
//          // console.log(controller)
//          timeline.fromTo($(this), controller.duration, controller.from, controller.to, controller.delay).pause();
//          // controller.delay
//         });


//         if($this.data("timeline").trigger == "scroll"){
//          triggerZanimationTimeline($this, timeline);
//          $(window).on('scroll', function(){triggerZanimationTimeline($this, timeline)});
//      }

//     });
// }






(function($) {
	"use strict";
	$.fn.zanimationSplit = function(option) {

		var $this       = this,
			controller  = $this.data("zanim-text"),
			split       = new SplitText($this, {type: 'lines, words, chars'});

		controller.delay || (controller.delay = 0.02);
		controller.split || (controller.split = "chars");
		controller.ease && (controller.to.ease = controller.ease) && controller.to.ease || (controller.to.ease = 'Expo.easeOut');

		// split[controller.split].css('opacity', '0');

		function triggerAnimation(){
			if(isElementInViewport($this) && $this.attr('data-zanim-text')) {
				TweenMax.staggerFromTo(split[controller.split], controller.duration, controller.from, controller.to, controller.delay, function(){
					split.revert();
				});
				$this.removeAttr('data-zanim-text');
			}
		}

		triggerAnimation();
		$(window).on('scroll', triggerAnimation);
	}
}(jQuery));







(function($){
	"use strict";
	$.fn.inertia = function(controller) {

		var $this = this,
			options = $this.data("inertia"),
			offset = $this.offset().top,
			winHeight = $(window).height(),
			currentPosition = $(window).scrollTop(),
			y = 0,
			previousPosition = 0;

	// function getController(el, options){
	//  var $this   = $(el),
	//      controller = $this.data("zanim");
		
	//  if (options === undefined) { 
	//      options = {delay: 0, duration: 0.8, ease: 'Expo.easeOut', from:{}, to:{}}; 
	//  }


	//  //populating the controller
	//  controller.delay || (controller.delay = options.delay);
	//  controller.duration || (controller.duration = options.duration);
	//  controller.from || (controller.from = options.from);
	//  controller.to || (controller.to = options.to);
	//  controller.ease && (controller.to.ease = controller.ease) && controller.to.ease || (controller.to.ease = options.ease);
		
	//  return controller;
	// }

	// function isScrolledIntoView($this){

	// 	var $elem = $this,
	// 		windowHeight = $(window).height(),
	// 		elemTop = $elem.offset().top,
	// 		elemHeight = $elem.height();
	// 		windowScrollTop = $(window).scrollTop();

	// 	if(elemTop <= (windowScrollTop + windowHeight) && windowScrollTop <= (elemTop + elemHeight)){
	// 		return true;
	// 	}
	// 	return false;
	// }

		options && (controller = options) || !controller && (controller = {});
		controller.weight || (controller.weight = 2);
		controller.duration || (controller.duration = 0.7);
		controller.ease || (controller.ease = "Power3.easeOut");

		$this.css('transform', 'translateY('+(($this.offset().top - $(window).scrollTop())*100/winHeight)+'px)');

		$(window).on("resize scroll", function(){

			currentPosition = $(window).scrollTop();
			y = controller.weight * (offset - currentPosition)*100/winHeight;

			(currentPosition == previousPosition) || TweenMax.to($this, controller.duration, {y: y, ease: controller.ease});

			previousPosition = currentPosition;

		});
	}
}(jQuery));
