(function(){
    'use strict';

    angular.module('scrumboard.demo',['ngRoute'])
    .controller('ScrumboardController', ['$scope', '$http', ScrumboardController]);

    function ScrumboardController($scope, $http) {
        $scope.add = function (list, title){
            var card = {
                list: list.id,
                title: title
            };
            $http.post('/scrumboard/cards/', card)
            .then(function(response){
                list.cards.push(response.data);
            },
            function(){
                alert('Couldnot create card');
            }
            );            
        };

        $scope.login = function() {
            alert('Couldnot create card');        
        };

       $scope.data = [];
       $http.get('/scrumboard/lists/').then(
           function(response){
           $scope.data = response.data;
       });
    }
}());
