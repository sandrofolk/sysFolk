(function(){
    'use strict';

    angular
        .module('app.person')
        .factory('PersonServices', PersonServices)


    function PersonServices($q, $http, personApi, $timeout){

        var model = {
            data: [],
            get: get,
            load: load,
            add: add,
            edit: edit,
            remove: remove
        }

        function get(id){
            var deferred = $q.defer()
            if (id){
                $http
                    .get(personApi + id + '/')
                    .then(
                        function(response){
                            model.data = response.data
                            deferred.resolve(model)
                        },
                        function(error){
                            deferred.reject(error.data)
                        }
                    )
            } else {
                $timeout(function(){
                    model.data = {}
                    deferred.resolve(model)
                },100)
            }

            return deferred.promise            
        }

        function load(){
            var deferred = $q.defer()
            $http
                .get(personApi)
                .then(
                    function(response){
                        model.data = response.data
                        deferred.resolve(model)
                    },
                    function(error){
                        deferred.reject(error.data)
                    }
                )
            return deferred.promise
        }

        function add(postObject){
            return $http.post(personApi, postObject)
        }

        function edit(dataObject){
            return $http.put(personApi + dataObject.id + '/', dataObject)
        }

        function remove(id){
            return $http.delete(personApi + id + '/')
        }

        return model
    }

}());