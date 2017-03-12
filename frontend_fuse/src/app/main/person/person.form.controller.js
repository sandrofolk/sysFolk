(function(){
    'use strict';

    angular
        .module('app.person')
        .controller('PersonFormController', PersonFormController)


    function PersonFormController($scope, person, $state){
        var vm = this;
        vm.form = person.data
        var is_editing = Object.keys(person.data).length > 0

        vm.isFormValid = function(formName)
        {
            if ( $scope[formName] && $scope[formName].$valid )
            {
                return $scope[formName].$valid;
            }
        }

        vm.save = function(){
            if (is_editing){
                person.edit(vm.form)
                    .then(
                        function(){
                            swal({
                                title: 'Beleza!',
                                text: 'Registro Salvo!',
                                type: 'success',
                                timer: 2000,
                                showConfirmButton: false,
                            })
                            $state.go('app.person.list',{}, {reload: true})
                        },
                        function(error){
                            swal({
                                title: 'Ops!',
                                text: error.data.detail,
                                type: 'error'
                            })
                        }
                    )
            } else {
                person.add(vm.form)
                    .then(
                        function(){
                            swal({
                                title: 'Beleza!',
                                text: 'Registro Salvo!',
                                type: 'success',
                                timer: 2000,
                                showConfirmButton: false,
                            })
                            $state.go('app.person.list',{}, {reload: true})
                        },
                        function(error){
                            swal({
                                title: 'Ops!',
                                text: error.data.detail,
                                type: 'error'
                            })
                        }
                    )            
            }
        }

    }

}());