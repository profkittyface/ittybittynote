api_base = 'http://127.0.0.1:9000';

angular.module('IttyBittyNote').controller('noteController', function($scope, $http) {
    $scope.notes = [];
    $scope.newNote = {'title': '', 'content': ''}

    var createNote = function(title, content){
      $http.post(api_base+'/notes/',$scope.newNote)
      .then(function(response){
        console.log(response)
      }, function(error){
        console.log(error)
      })

    }

    var updateNotes = function() {
        $http.get('http://127.0.0.1:9000/notes')
            .then(function(response) {
                console.log(response)
                $scope.notes = response.data
            }, function(error) {
                console.log(error)
            })
    };
    updateNotes();
    createNote($scope.newNote.title, $scope.newNote.content);
    });
