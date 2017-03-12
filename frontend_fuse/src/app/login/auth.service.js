(function(){
    'use strict';
    var serverUrl = config_data.protocol + config_data.address + ':' + config_data.port + '/'
    var urlAuth = serverUrl + 'rest-auth/'
    var urlUser = serverUrl + 'api/user/'

    angular
        .module('app.pages.auth.login')
        .factory('AuthServices', AuthServices)

    function AuthServices($q, $http, localStorageService){
        var model = {
            is_logged: false,
            profile: {},
            signIn: signIn,
            signOut: signOut,
            check: check,
        }

        return model

        function signIn(userInfo){
            var deferred = $q.defer()
            $http
                .post(urlAuth + 'login/', userInfo)
                .then(
                    function(response){
                        localStorageService.set('token', response.data.key)
                        model.is_logged = true
                        deferred.resolve(model)
                    },
                    function(error){
                        localStorageService.clearAll()
                        model.is_logged = false
                        deferred.reject(error)
                    }
                )

            return deferred.promise
        }

        function signOut(){
            var deferred = $q.defer()
            $http
                .post(urlAuth + 'logout/')
                .then(
                    function(){
                        localStorageService.clearAll()
                        model.is_logged = false
                        deferred.resolve()
                    },
                    function(){
                        localStorageService.clearAll()
                        model.is_logged = false
                        deferred.resolve()
                    }
                )

            return deferred.promise
        }

        function check(){
            var deferred = $q.defer()

            $http
                .get(urlAuth + 'user/')
                .then(
                    function(response){
                        var user = response.data
                        $http
                            .get(urlUser + user.pk + '/')
                            .then(
                                function(userResponse){
                                    model.profile = userResponse.data
                                    model.is_logged = true

                                    deferred.resolve(model)
                                },
                                function(userError){
                                    sigout()

                                    deferred.reject(userError)
                                }
                            )
                    },
                    function(error){
                        sigout()

                        deferred.reject(error)
                    }
                )

            return deferred.promise
        }
    }

}());