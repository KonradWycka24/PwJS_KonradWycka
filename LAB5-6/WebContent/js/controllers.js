var portfolioApp= angular.module('PortfolioApp',[]);
portfolioApp.controller('GalleryListCtrl', function($scope) {
    $scope.galleries = [
    { 'title':'Something',
     'when':'2015-12-14',
     'thumbnailUrl':'\img\i\Castle in the space.png'
    },

    { 'title':'Crystal Knight',
     'when':'2014-08-04',
     'thumbnailUrl':'/img/i/Crystal knight.png'
    },

    { 'title':'Dragon',
    'when':'2014-08-04',
    'thumbnailUrl':'/img/i/Dragon.png'
    },

   { 'title':'Radioactive',
   'when':'2014-08-04',
   'thumbnailUrl':'/img/i/Radioactive.png'
   },

   { 'title':'Ring',
  'when':'2014-08-04',
  'thumbnailUrl':'/img/i/Ring.png'
   },

 { 'title':'Void Beast',
 'when':'2014-08-04',
 'thumbnailUrl':'/img/i/voidgod.png'
 }
];}); 