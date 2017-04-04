angular.module('IttyBittyNote').controller('noteController', function($scope, $http) {
    $scope.notes = [];

    var updateNotes = function() {
        $http.get('http://localhost:5000/notes')
            .then(function(response) {
                console.log(response)
                $scope.notes = response.data
            }, function(error) {
                console.log(error)
            })
    };
updateNotes();
});
