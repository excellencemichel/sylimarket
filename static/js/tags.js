 $(document).ready(function(){

 	var tagForm = $(".form-tag-ajax")

 	tagForm.submit(function(event){
 		event.preventDefault()

 		var thisTag = $(this)

 		var tagEndpoint = thisTag.attr("data-endpoint")
 		var tagHTTPMethod = thisTag.attr("method")
 		var tagData = thisTag.serialize();

 		$.ajax({
 			url: tagEndpoint,
 			method: tagHTTPMethod,
 			data: tagData,

 			success: function(data){
 				$.alert({
		        title: "Super !",
		        content: "Le produit a bien été tagé",
		        theme: "modern",
        })

 			},

 			error: function(error){
 				$.alert({
          		title: "oops !",
          		content: "Une erreur s'est occasionée",
          		theme: "modern",
        })
 			}
 		})
 	})


var wishForm = $(".form-wish-ajax")

  wishForm.submit(function(event){
    event.preventDefault()

    var thisWish = $(this)
    var wishEndpoint = thisWish.attr("data-endpoint")
    var wishUrl       = thisWish.attr("method")
    var wishData = thisWish.serialize();

    $.ajax({
            url: wishEndpoint,
      method: wishUrl,
      data: wishData,

      success: function(data){
        var submitSpan = thisWish.find(".submit-span")
        if(data.added){
                  submitSpan.html('<button type="submit" style="color: #0f6bb2; background-color: #0f6bb2; border: none;"><a data-toggle="tooltip" class="add-to-cart" href="#" title="Déjà dans la liste de souhaits"> <i class="icon fa fa-heart" style="color:red;"></i></a></button>')
        }else{
                  submitSpan.html('<button type="submit" style="color: #0f6bb2; background-color: #0f6bb2; border: none;"><a data-toggle="tooltip" class="add-to-cart" href="#" title="Pas encore de souhaits"> <i class="icon fa fa-heart"></i> </a></button>')

        }
      },


      error: function(errorData){
        $.alert({
          title: "oops !",
          content: "Une erreur s'est occasionée",
          theme: "modern",
        })
      }


    })
  })




})