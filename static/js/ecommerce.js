 $(document).ready(function(){

    
  // Auto Search

  var searchForm = $(".query-search-form")

  var searchInput = searchForm.find("[name='q']") // input name='q'


  // debut de ma merde
  var categorieSearchText = searchForm.find(".categorie-search-text")
  var categorieMenuItem = searchForm.find(".category-menuitem")
  var categoryProduct = searchForm.find("[name='category-product']")


  console.log(categorieSearchText.text());


   $(".query-search-form .category-menuitem").click(function (event) {
     categoryProduct.val(this.text)
     console.log("La catégory est :", categoryProduct.val());
     perforSearchMerde()
     categorieSearchText.html(this.text + '<b class="caret">')

   })

   function perforSearchMerde() {
     displaySearching()
     var query = categoryProduct.val()
     console.log("Le query est", query);
     


     setTimeout(function () {

       window.location.href = "/search/?q=" + query
     }, 1000)
   }
/*
Ma merde
   */

  var typingTimer;
  var typingInterval = 500 // 
  var searchBtn = searchForm.find("[type='submit']")


  searchInput.keyup(function(event){
    //key released
    clearTimeout(typingTimer)

    typingTimer = setTimeout(perforSearch, typingInterval)
    
    
  })

  searchInput.keydown(function(event){
    // key pressed
    clearTimeout(typingTimer)
  })

  function displaySearching(){
    searchBtn.addClass("disabled")
    searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
  }

  function perforSearch(){
    displaySearching()
    var query = searchInput.val()


    setTimeout(function(){

    window.location.href="/search/?q=" + query
    }, 1000)
  }




  //Test demo ajax

  var toggleVar = $(".toggle-item")
  var inputQty = $("#product-qty-input")
  toggleVar.click(function(event){
    event.preventDefault()
    thisInput = $(this)
    console.log("L'evenement", event)

    var qtyUrl = "/cart/demo"
    var qtyMethod = "POST"
    var data = thisInput.text()
    $.ajax({
      url: qtyUrl,
      data: data,

      success: function(data){
        console.log("La fonction ajax avec input s'est exécuté")
        console.log(data)
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


  // Partie de la gestion des liste de souhaits

  var wishForm = $(".form-wish-ajax")

  wishForm.submit(function(event){
    event.preventDefault()

    var thisWish = $(this)
    var wishEndpoint = thisWish.attr("data-endpoint")
    var wishHTTPMethode       = thisWish.attr("method")
    var wishData = thisWish.serialize();

    $.ajax({
            url: wishEndpoint,
      method: wishHTTPMethode,
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


  // Partie de la gestion des tags

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

        $("#exampleInputTag").val("")

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




        // Start add product to cart
      var productForm = $(".form-product-ajax")
      var forQty = $(".for-qty")

      productForm.submit(function(event){
          event.preventDefault()
          var thisForm = $(this)
          // var actionEndpoint = thisForm.attr("action")
          var actionEndpoint = thisForm.attr("data-endpoint")
          var httpMethod = thisForm.attr("method")
          var formData = thisForm.serialize();
              $.ajax({
                url : actionEndpoint,
                method: httpMethod,
                data: formData,
                success: function(data){
                var submitSpan = thisForm.find(".submit-span")
                if (data.added){
                  submitSpan.html('<button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;"><i class="fa fa-times"></i></span>Enlever</button>')
                } else {
                  submitSpan.html('<button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;"><span><i class="fa fa-plus-circle"></i></span>Ajouter</button>')
                }

                var navbarCount = $(".navbar-cart-count")
                navbarCount.text(data.cartItemCount)


                currentPath = window.location.href

                if (currentPath.indexOf("cart") != -1){
                  refreshCart()
                }


                var navBarCount = $(".navbar-cart-count")
                var navBarCartSommeTotal = $(".cart-somme-total")
                navBarCount.text(data.cartItemCount)
                navBarCartSommeTotal.text(data.cartTotal)
                },

                error: function(errorData){
                  $.alert({
                    title:"Oops !",
                    content:
                    "An error occured",
                    theme: "modern"})
                  
                }
              })

      })

      // End add product to cart




      function refreshCart(){
        var cartTableHomeSomme = $(".cart-table-home-somme")
        var cartTableHome = $(".cart-table-home")
        var cartBodyHome = cartTableHome.find(".cart-body-home")
        var productRows = cartBodyHome.find(".cart-product-home")
        var currentUrl = window.location.href

        var refreshCartUrl = "/cart/api/cart/"
        var refreshCartMethod = "GET"
        var data = {}
        $.ajax({
          url : refreshCartUrl,
          method: refreshCartMethod,
          data: data,
          success : function(data){
            var hiddenCartRemoveForm = $(".cart-item-remove-form")
            if(data.products.length > 0){

            productRows.html(" ")
            i = 1
            $.each(data.products, function(index, value){
              var newCartItemRemove = hiddenCartRemoveForm.clone()
              newCartItemRemove.css("display", "block")
              newCartItemRemove.find(".cart-item-product-id").val(value.id)
              newCartItemRemove.find(".product-qty-input").val(value.quantite)
              cartBodyHome.prepend("<tr><td class='romove-item'>" + newCartItemRemove.html() + " <td class='cart-image'><a class='entry-thumbnail' href='" + value.url +"'><img src='" + value.image + "' alt=''></a></td><td class='cart-product-name-info'><h4 class='cart-product-description'><a href='" + value.url + "'>" + value.name + "</a></h4></td><td class='cart-product-edit'><a href='" + value.url + "'class='product-edit'>Modifier</a></td><td class='cart-product-quantity'><div class='cart-quantity'><div class='quant-input'><strong> X " + data.quantite[value.id]  + "</strong></div></div></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.price + "</span></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.taxe + "</span></td><td class=cart-product-grand-total><span class=cart-grand-total-price>$" + parseFloat(value.subtotal) * parseFloat(data.quantite[value.id])  + "</span></td></tr> " )

            })

            cartTableHomeSomme.find(".cart-subtotal-home-somme").text(data.subtotal)
            cartTableHomeSomme.find(".cart-subtotal-home-taxe").text(data.taxe)
            cartTableHomeSomme.find(".cart-total-home-somme").text(data.total)

            totalText = cartBodyHome.find(".cart-total-home").text()

            }
            else{
              window.location.href = currentUrl
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

      }


      // End remove product from cart











       var payementMethodContainer = $(".checkout-step-01")
       var payementMethodForm = payementMethodContainer.find("#collapseOne")
       var payementMethodLink = payementMethodForm.find(".payement-method-link")
       var billingContainer = $(".checkout-step-02")
       var billinForm = billingContainer.find("#collapseTwo")
       var billinLink = billinForm.find(".billing-link")
       console.log()


       var payementForm = $(".payement-choice-form")

      payementForm.submit(function(event){
        event.preventDefault()
        var inputs = payementForm.find("input")
        var payementMethodChoice = payementForm.find("[name='payementmethod']")
        // console.log("La valeur est:", payementMethodChoice.checked)


        var hiddenFacturationlivraison = $(".payement-method-livraison")
        var hiddenFacturationBancaire = $(".payement-method-bancaire")
        var hiddenFacturationMobile = $(".payement-method-mobile")
        var facturationAddress = $(".facturation-address")
        
        facturationAddress.html(" ")
        $.each(payementMethodChoice, function(index,choix){
          if (choix.checked){
            payementMethodForm.removeClass("in")
            payementMethodLink.addClass("collapsed")
            billinForm.addClass("in")
            billinLink.removeClass("collapsed")
            console.log("Un choix")
            console.log(choix.value)
            if(choix.value == "livraison"){
            
                var newFacturationLivraisonForm = hiddenFacturationlivraison.clone()
                newFacturationLivraisonForm.css("display", "block")


                facturationAddress.prepend(newFacturationLivraisonForm.html())
            }

            else if(choix.value == "bancaire"){
                var newFacturationBancaireForm = hiddenFacturationBancaire.clone()
                newFacturationBancaireForm.css("display", "block")

                facturationAddress.prepend(newFacturationBancaireForm.html())
            }

            else if(choix.value == "mobile"){
                var newFacturationMobileForm = hiddenFacturationMobile.clone()
                newFacturationMobileForm.css("display", "block")


                facturationAddress.prepend(newFacturationMobileForm.html())

              }

              else{
                alert("Vous devez faire un choix de payement !")
              }



          }
          else if(!choix.checked){
            console.log("Pas de choix")

          }


        })


      })



  })
