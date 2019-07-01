 $(document).ready(function(){


    
  // Auto Search

  var searForm = $(".query-search-form")

  var searchInput = searForm.find("[name='q']") // input name='q'

  var typingTimer;
  var typingInterval = 500 // 
  var searchBtn = searForm.find("[type='submit']")

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
  console.log("Mon toggleVar",toggleVar.length)
  var inputQty = $("#product-qty-input")
  console.log("La quantité", inputQty)
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


        // Start add product to cart
      var productFormAdd = $(".form-product-ajax")
      var forQty = $(".for-qty")

      productFormAdd.submit(function(event){
          event.preventDefault()
          var thisForm = $(this)
          // var actionEndpoint = thisForm.attr("action")
          var actionEndpoint = thisForm.attr("data-endpoint")
          var httpMethod = thisForm.attr("method")
          var formData = thisForm.serialize();
              // $.ajax({
              //   url : actionEndpoint,
              //   method: httpMethod,
              //   data: formData,
              //   success: function(data){
              //   var submitSpan = thisForm.find(".submit-span")
              //   if (data.added){
              //     submitSpan.html('<button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;"><i class="fa fa-times"></i></span> Enlever du panier</button>')
              //   } else {
              //     submitSpan.html('<button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;"><span><i class="fa fa-plus-circle"></i></span> Ajouter au panier</button>')
              //   }

              //   var navbarCount = $(".navbar-cart-count")
              //   navbarCount.text(data.cartItemCount)


              //   currentPath = window.location.href

              //   if (currentPath.indexOf("cart") != -1){
              //     refreshCart()
              //   }
              //   },

              //   error: function(errorData){
              //     $.alert({
              //       title:"Oops !",
              //       content:
              //       "An error occured",
              //       theme: "modern"})
                  
              //   }
              // })

          $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function(data){
              var submitSpan = thisForm.find(".submit-span")
                var spnQty = forQty.find(".submit-for-qty")
                  if(!data.stock_finish){
                    if (data.added){
                      submitSpan.html('<input type="hidden" name="for_remove_product" value="removed"><button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;">Enlever</button>')
                    } 
                  else {
                    submitSpan.html('<input type="hidden" name="for_add_product" value="added"><button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;">Add to cart</button>')
                    if (data.removed){
                      
                    var quantiteCount = $(".product-qty-input")
                    quantiteCount.val("1")
                    }

                      }

                  if(data.quantited){
                      spnQty.html('<input type="hidden" name="for_remove_product" value="removed"><button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;">Enlever</button>')
                  }

                  if(data.minimum){
                      $.alert({
                        title: "Erreur d'entrée de quantité",
                        content: "La quantité du produit entrée ne doit pas être inferieur à 1",
                        theme: "modern",
                        })

                    } 

                  if(data.no_number_quantite){
                      spnQty.html('<input type="hidden" name="for_add_product" value="added"><button type="submit" class="btn btn-primary cart-btn" style="display: inline-block;">Add to cart</button>')
                      $.alert({
                        title: "Erreur d'entrée de quantité",
                        content: "La quantité du produit entrée doit être un nombre et superieur ou égale à 1",
                        theme: "modern",
                        })

                    } 


                }
                else{
                   $.alert({
                title: "oops !",
                content: "Votre commande dépasse notre stock nous vous conseillons de la completer avec soit le même produit mais de couleur/marque différentes. Au plaisir nous allons faire un réapprovisionnement dans sous peu. Merci",
                theme: "modern",
              })
                }



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
                title: "oops !",
                content: "Une erreur s'est occasionée",
                theme: "modern",
              })
            }
          })
      })

      // End add product to cart


      function qtyChange(qtyForm) {
        // Pour le traitement de la quantité

        var actionEndpoint = qtyForm.attr("data-endpoint")
        var httpMethod = qtyForm.attr("method")
        var formData = qtyForm.serialize();
        var qtyContent = qtyForm.find("#product-qty-input")



      }



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
              cartBodyHome.prepend("<tr><td class='romove-item'>" + newCartItemRemove.html() + " <td class='cart-image'><a class='entry-thumbnail' href='" + value.url +"'><img src='" + value.image + "' alt=''></a></td><td class='cart-product-name-info'><h4 class='cart-product-description'><a href='" + value.url + "'>" + value.name + "</a></h4></td><td class='cart-product-edit'><a href='" + value.url + "'class='product-edit'>Edit</a></td><td class='cart-product-quantity'><div class='cart-quantity'><div class='quant-input'><strong> X " + data.quantite[value.id]  + "</strong></div></div></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.price + "</span></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.taxe + "</span></td><td class=cart-product-grand-total><span class=cart-grand-total-price>$" + parseFloat(value.subtotal) * parseFloat(data.quantite[value.id])  + "</span></td></tr> " )

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




  // var header = document.querySelector('.ui__header')

  // window.addEventListener('scroll' , function () {
  //   var headerHeight = header.getBoundingClientRect().height ;
  //   var scrollY = window.scrollY ;
  //   console.log(headerHeight , scrollY) ;
  //   if (scrollY > headerHeight) {
  //     if (header.classList.contains('ui__fix__header')) { return ; }
  //     header.classList.add('ui__fix__header') ;
  //   }else {
  //     if (!header.classList.contains('ui__fix__header')) { return ; }
  //     header.classList.remove('ui__fix__header') 
  //   }
  // })