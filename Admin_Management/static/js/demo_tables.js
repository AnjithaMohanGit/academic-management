
    function delete_row(dept_id){
        
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").off("click").on("click",function(){
            box.removeClass("open");

        var delete_url= document.getElementById("durl").value;
        // document.getElementById("txtid").value=dept_id;

        $.ajax({
                type: 'GET',
                url: delete_url,  // Update the URL according to your Django URL pattern
                data: {
                    'id': dept_id,
                   
                },
                success: function (data) {
                    // If successful, remove the table row
                if('success' in data){
                    $('#trow' + dept_id).hide("slow", function () {
                        $(this).remove();
                    });
                    alert(data.success)
                    location.reload(true);

                }
                else {
                    alert('Error: ' + data.error);
                }
                },
                error: function (error) {
                    console.log(error)
                }
            });
        });
    }


    function editdept(dept_id) {
        document.getElementById("txtid").value=dept_id;
        document.getElementById('spinner'+dept_id).className="fa fa-spinner";
        // var name=$("#name").val();
        var req_url= document.getElementById("url").value;
        $.ajax({
            type: "GET",
            url:req_url,
            data: {'id':dept_id},
            dataType: "json",
            success: function(data) {
                document.getElementById("edit_name").value=data.name;
                document.getElementById("edit_code").value=data.code;
                document.getElementById("edit_status").value=data.status;
                $('#modal_basic').modal('show');
                document.getElementById('spinner'+dept_id).className="fa fa-pencil";


              
            },
            error: function (error) {
                console.log(error)
            }
        });

    }




    // Assuming you have a function to handle updating cells in the table using AJAX
function updateCell() {

    var update_url= document.getElementById("up_url").value;
    var depid=document.getElementById('txtid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': depid,
            'new_name': document.getElementById("edit_name").value,
            'new_code': document.getElementById("edit_code").value,
            'new_status': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.message,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }
        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}


function edit_designation(des_id) {
    document.getElementById("txid").value=des_id;
    document.getElementById('spinner'+des_id).className="fa fa-spinner";
    // var name=$("#name").val();
    var req_url= document.getElementById("edit_url").value;
    $.ajax({
        type: "GET",
        url:req_url,
        data: {'id':des_id},
        dataType: "json",
        success: function(data) {
            document.getElementById("edit_dname").value=data.desname;
            document.getElementById("edit_dcode").value=data.descode;
            document.getElementById("edit_status").value=data.desstatus;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+des_id).className="fa fa-pencil";


          
        },
        error: function (error) {
            console.log(error)
        }
    });

}



function updatedesignation() {

    var update_url= document.getElementById("updes_url").value;
    var desid=document.getElementById('txid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': desid,
            'desname': document.getElementById("edit_dname").value,
            'descode': document.getElementById("edit_dcode").value,
            'desstatus': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            // Handle success response
          
            // console.log(data)
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.error,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }



            // Update the UI or display a message upon successful update
        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}


function desig_delete_row(des_id){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url= document.getElementById("del_url").value;
    // document.getElementById("txtid").value=dept_id;

    $.ajax({
            type: 'GET',
            url: delete_url,  // Update the URL according to your Django URL pattern
            data: {
                'id': des_id,
               
            },
            success: function (data) {
                // If successful, remove the table row
            if('success' in data){
                $('#trow' + des_id).hide("slow", function () {
                    $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else {
                alert('Error: ' + data.error);
            }
            },
            error: function (error) {
                console.log(error)
            }
        });
    });
}


function edit_qualification(q_id) {
    document.getElementById("txid").value=q_id;
    document.getElementById('spinner'+q_id).className="fa fa-spinner";
    // var name=$("#name").val();
    var req_url= document.getElementById("qedit_url").value;
    $.ajax({
        type: "GET",
        url:req_url,
        data: {'id':q_id},
        dataType: "json",
        success: function(data) {
            document.getElementById("edit_qname").value=data.qua_name;
            document.getElementById("edit_status").value=data.qua_status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+q_id).className="fa fa-pencil";


          
        },
        error: function (error) {
            console.log(error)
        }
    });

}


function updatequalification() {

    var update_url= document.getElementById("up_qua_url").value;
    var qid=document.getElementById('txid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': qid,
            'qua_name': document.getElementById("edit_qname").value,
            'qua_status': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            // Handle success response
          
            // console.log(data)
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.error,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }

        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}


function delete_row(qua_id){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url= document.getElementById("qdel_url").value;
    // document.getElementById("txtid").value=dept_id;

    $.ajax({
            type: 'GET',
            url: delete_url,  // Update the URL according to your Django URL pattern
            data: {
                'id': qua_id,
               
            },
            success: function (data) {
                // If successful, remove the table row
            if('success' in data){
                $('#trow' + qua_id).hide("slow", function () {
                    $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else {
                alert('Error: ' + data.error);
            }
            },
            error: function (error) {
                console.log(error)
            }
        });
    });
}

function edit_class(c_id) {
    document.getElementById("txid").value=c_id;
    document.getElementById('spinner'+c_id).className="fa fa-spinner";
    // var name=$("#name").val();
    var req_url= document.getElementById("cedit_url").value;
    $.ajax({
        type: "GET",
        url:req_url,
        data: {'id':c_id},
        dataType: "json",
        success: function(data) {
            document.getElementById("edit_class").value=data.class_name;
            document.getElementById("edit_status").value=data.class_status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+c_id).className="fa fa-pencil";


          
        },
        error: function (error) {
            console.log(error)
        }
    });

}

function updateclass() {

    var update_url= document.getElementById("up_cls_url").value;
    var cid=document.getElementById('txid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': cid,
            'class_name': document.getElementById("edit_class").value,
            'class_status': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            // Handle success response
          
            // console.log(data)
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.error,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }

        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}


function class_delete_row(c_id){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url= document.getElementById("cdel_url").value;
    // document.getElementById("txtid").value=dept_id;

    $.ajax({
            type: 'GET',
            url: delete_url,  // Update the URL according to your Django URL pattern
            data: {
                'id': c_id,
               
            },
            success: function (data) {
                // If successful, remove the table row
            if('success' in data){
                $('#trow' + c_id).hide("slow", function () {
                    $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else {
                alert('Error: ' + data.error);
            }
            },
            error: function (error) {
                console.log(error)
            }
        });
    });
}

function edit_division(d_id) {
    document.getElementById("txid").value=d_id;
    document.getElementById('spinner'+d_id).className="fa fa-spinner";
    // var name=$("#name").val();
    var req_url= document.getElementById("div_edit_url").value;
    $.ajax({
        type: "GET",
        url:req_url,
        data: {'id':d_id},
        dataType: "json",
        success: function(data) {
            document.getElementById("edit_div").value=data.div_name;
            document.getElementById("edit_status").value=data.div_status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+d_id).className="fa fa-pencil";


          
        },
        error: function (error) {
            console.log(error)
        }
    });

}


function updatedivision() {

    var update_url= document.getElementById("up_div_url").value;
    var did=document.getElementById('txid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': did,
            'div_name': document.getElementById("edit_div").value,
            'div_status': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            // Handle success response
          
            // console.log(data)
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.error,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }

        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}


function division_delete_row(d_id){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");
   
    var delete_url= document.getElementById("div_del_url").value;
    // document.getElementById("txtid").value=dept_id;

    $.ajax({
            type: 'GET',
            url: delete_url,  // Update the URL according to your Django URL pattern
            data: {
                'id': d_id,
               
            },
            success: function (data) {
                // If successful, remove the table row
            if('success' in data){
                $('#trow' + d_id).hide("slow", function () {
                    $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else {
                alert('Error: ' + data.error);
            }
            },
            error: function (error) {
                console.log(error)
            }
        });

        
    });
    
}


function edit_emp_category(e_id) {
    document.getElementById("txid").value=e_id;
    document.getElementById('spinner'+e_id).className="fa fa-spinner";
    // var name=$("#name").val();
    var req_url= document.getElementById("edit_emp_url").value;
    $.ajax({
        type: "GET",
        url:req_url,
        data: {'id':e_id},
        dataType: "json",
        success: function(data) {
            document.getElementById("edit_emp_cat").value=data.emp_cat_name;
            document.getElementById("edit_area").value=data.emp_cat_area;
            document.getElementById("edit_status").value=data.emp_status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+e_id).className="fa fa-pencil";


          
        },
        error: function (error) {
            console.log(error)
        }
    });

}

function update_emp_cat() {

    var update_url= document.getElementById("up_emp_url").value;
    var uid=document.getElementById('txid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': uid,
            'emp_name': document.getElementById("edit_emp_cat").value,
            'emp_area': document.getElementById("edit_area").value,
            'emp_status': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            // Handle success response
          
            // console.log(data)
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.error,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }



            // Update the UI or display a message upon successful update
        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}

function emp_delete_row(e_id){
        
    var box = $("#mb-remove-row");
    box.addClass("open");
    
    box.find(".mb-control-yes").off("click").on("click",function(){
        box.removeClass("open");

    var delete_url= document.getElementById("del_emp_url").value;
    // document.getElementById("txtid").value=dept_id;

    $.ajax({
            type: 'GET',
            url: delete_url,  // Update the URL according to your Django URL pattern
            data: {
                'id': e_id,
               
            },
            success: function (data) {
                // If successful, remove the table row
            if('success' in data){
                $('#trow' + e_id).hide("slow", function () {
                    $(this).remove();
                });
                alert(data.success)
                location.reload(true);

            }
            else {
                alert('Error: ' + data.error);
            }
            },
            error: function (error) {
                console.log(error)
            }
        });
    });
}

function editsubject(s_id) {
    document.getElementById("txid").value=s_id;
    document.getElementById('spinner'+s_id).className="fa fa-spinner";
    // var name=$("#name").val();
    var req_url= document.getElementById("sedit_url").value;
    $.ajax({
        type: "GET",
        url:req_url,
        data: {'id':s_id},
        dataType: "json",
        success: function(data) {
            document.getElementById("edit_subject").value=data.sub_name;
            document.getElementById("edit_class").value=data.class_details;
            document.getElementById("edit_status").value=data.sub_status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+s_id).className="fa fa-pencil";


          
        },
        error: function (error) {
            console.log(error)
        }
    });

}

function updatesubject() {

    var update_url= document.getElementById("up_sub_url").value;
    var uid=document.getElementById('txid').value;
    
    $.ajax({
        url: update_url,
        type: 'GET',
        data: {
            'id': uid,
            'sub_name': document.getElementById("edit_subject").value,
            'sub_class': document.getElementById("edit_class").value,
            'sub_status': document.getElementById("edit_status").value
        },
        dataType: 'json',
        success: function(data) {
            // Handle success response
          
            // console.log(data)
            
            if('success' in data) { 
                noty({
                    text: data.success,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'success',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            } else {
                noty({
                    text: data.error,
                    layout: 'topRight',
                    timeout: 1000,
                    type: 'error',
                    callback: {
                        afterShow: function () {
                            setTimeout(function () {
                                location.reload(true);
                            }, 2000);
                        }
                    }
                }).show();
            }



            // Update the UI or display a message upon successful update
        },
        error: function(error) {
            // Handle error response
            console.error('Error:', error);
            
        }
        
    });
}






















