/*------------------------------------------------------
    Author : www.webthemez.com
    License: Commons Attribution 3.0
    http://creativecommons.org/licenses/by/3.0/
---------------------------------------------------------  */

(function ($) {
    "use strict";
    var mainApp = {

        initFunction: function () {
            /*MENU 
            ------------------------------------*/
            $('#main-menu').metisMenu();
			
            $(window).bind("load resize", function () {
                if ($(this).width() < 768) {
                    $('div.sidebar-collapse').addClass('collapse')
                } else {
                    $('div.sidebar-collapse').removeClass('collapse')
                }
            });

            /* MORRIS BAR CHART
			-----------------------------------------*/
            Morris.Bar({
                element: 'morris-bar-chart',
                data: [{
                    y: '2006',
                    a: 100,
                    b: 90
                }, {
                    y: '2007',
                    a: 75,
                    b: 65
                }, {
                    y: '2008',
                    a: 50,
                    b: 40
                }, {
                    y: '2009',
                    a: 75,
                    b: 65
                }, {
                    y: '2010',
                    a: 50,
                    b: 40
                }, {
                    y: '2011',
                    a: 75,
                    b: 65
                }, {
                    y: '2012',
                    a: 100,
                    b: 90
                }],
                xkey: 'y',
                ykeys: ['a', 'b'],
                labels: ['Series A', 'Series B'],
				 barColors: [
    '#A6A6A6','#24C2CE',
    '#A8E9DC' 
  ],
                hideHover: 'auto',
                resize: true
            });
	 


            /* MORRIS DONUT CHART
			----------------------------------------*/
            Morris.Donut({
                element: 'morris-donut-chart',
                data: [{
                    label: "Download Sales",
                    value: 12
                }, {
                    label: "In-Store Sales",
                    value: 30
                }, {
                    label: "Mail-Order Sales",
                    value: 20
                }],
				   colors: [
    '#A6A6A6','#24C2CE',
    '#A8E9DC' 
  ],
                resize: true
            });

            /* MORRIS AREA CHART
			----------------------------------------*/

            Morris.Area({
                element: 'morris-area-chart',
                data: [{
                    period: '2016-04-01',
                    电量: 1723,

                }, {
                    period: '2016-04-04',
                    电量: 1725,

                }, {
                    period: '2016-04-07',
                    电量: 1738,

                }, {
                    period: '2016-04-10',
                    电量: 1742,

                }, {
                    period: '2016-04-13',
                    电量: 1746,

                }, {
                    period: '2016-04-16',
                    电量: 1755,

                }, {
                    period: '2016-04-19',
                    电量: 1768,

                }, {
                    period: '2016-04-22',
                    电量: 1777,

                }, {
                    period: '2016-04-25',
                    电量: 1795,

                }, {
                    period: '2016-04-28',
                    电量: 1823,

                }],
                xkey: 'period',
                ykeys: ['电量'],
                labels: ['电量'],
                pointSize: 2,
                hideHover: 'auto',
				  pointFillColors:['#ffffff'],
				  pointStrokeColors: ['black'],
				  lineColors:['#A6A6A6','#24C2CE'],
                resize: true
            });

            /* MORRIS LINE CHART
			----------------------------------------*/
            Morris.Line({
                element: 'morris-line-chart',
                data: [
					  { y: '2016-04-28 01:00', a: 0.55},
					  { y: '2016-04-28 03:00', a: 0.51},
					  { y: '2016-04-28 05:00', a: 0.47},
					  { y: '2016-04-28 07:00', a: 0.52},
					  { y: '2016-04-28 09:00', a: 0.57},
					  { y: '2016-04-28 11:00', a: 0.51},
					  { y: '2016-04-28 13:00', a: 0.53},
					  { y: '2016-04-28 15:00', a: 0.55},
					  { y: '2016-04-28 17:00', a: 0.57},
					  { y: '2016-04-28 19:00', a: 0.55},
					  { y: '2016-04-28 21:00', a: 0.51},
					  { y: '2016-04-28 23:00', a: 0.58}
				],
            
				 
      xkey: 'y',
      ykeys: ['a'],
      labels: ['湿度'],
      fillOpacity: 0.6,
      hideHover: 'auto',
      behaveLikeLine: true,
      resize: true,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','#24C2CE']
	  
            });
           
        
            $('.bar-chart').cssCharts({type:"bar"});
            $('.donut-chart').cssCharts({type:"donut"}).trigger('show-donut-chart');
            $('.line-chart').cssCharts({type:"line"});

            $('.pie-thychart').cssCharts({type:"pie"});
       
	 
        },

        initialization: function () {
            mainApp.initFunction();

        }

    }
    // Initializing ///

    $(document).ready(function () {
        mainApp.initFunction(); 
		$("#sideNav").click(function(){
			if($(this).hasClass('closed')){
				$('.navbar-side').animate({left: '0px'});
				$(this).removeClass('closed');
				$('#page-wrapper').animate({'margin-left' : '260px'});
				
			}
			else{
			    $(this).addClass('closed');
				$('.navbar-side').animate({left: '-260px'});
				$('#page-wrapper').animate({'margin-left' : '0px'}); 
			}
		});
    });

}(jQuery));
