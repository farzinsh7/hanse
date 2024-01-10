(function ($) {
	"use strict";
  
	function isElementInViewport(el) {
	  if (el instanceof jQuery) {
		el = el[0];
	  }
  
	  var rect = el.getBoundingClientRect();
  
	  return (
		rect.top >= 0 &&
		rect.left >= 0 &&
		rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
		rect.right <= (window.innerWidth || document.documentElement.clientWidth)
	  );
	}
  
	$.fn.zanimationSplit = function (options) {
	  var $this = this;
	  var controller = $this.data("zanim-text");
	  var split = new SplitText($this, { type: "lines, words, chars" });
  
	  controller = controller || {};
	  controller.delay = controller.delay || 0.02;
	  controller.split = controller.split || "chars";
	  controller.to = controller.to || {};
	  controller.to.ease = controller.ease || "Expo.easeOut";
  
	  function triggerAnimation() {
		if (isElementInViewport($this) && $this.attr("data-zanim-text")) {
		  TweenMax.staggerFromTo(
			split[controller.split],
			controller.duration,
			controller.from,
			controller.to,
			controller.delay,
			function () {
			  split.revert();
			}
		  );
		  $this.removeAttr("data-zanim-text");
		}
	  }
  
	  triggerAnimation();
	  $(window).on("scroll", triggerAnimation);
	};
  
	$.fn.inertia = function (options) {
	  var $this = this;
	  var controller = $this.data("inertia") || {};
	  controller.weight = controller.weight || 2;
	  controller.duration = controller.duration || 0.7;
	  controller.ease = controller.ease || "Power3.easeOut";
  
	  function updatePosition() {
		var offset = $this.offset().top;
		var winHeight = $(window).height();
		var currentPosition = $(window).scrollTop();
		var y = controller.weight * ((offset - currentPosition) * 100) / winHeight;
  
		if (currentPosition !== previousPosition) {
		  TweenMax.to($this, controller.duration, { y: y, ease: controller.ease });
		}
  
		previousPosition = currentPosition;
	  }
  
	  $this.css("transform", "translateY(" + (($this.offset().top - $(window).scrollTop()) * 100 / $(window).height()) + "px)");
  
	  $(window).on("resize scroll", updatePosition);
	};
  })(jQuery);
  