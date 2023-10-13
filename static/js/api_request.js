console.log("Sanity check!");

// Get Stripe publishable key
    fetch("/config/")
      .then((result) => {
        return result.json();
      })
      .then((data) => {
        // Initialize Stripe.js
        const stripe = Stripe(data.publicKey);

        // Event handler
        document.querySelector("#submitBtn").addEventListener("click", () => {
          // Get Checkout Session ID
          fetch("/create-checkout-session/")
            .then((result) => {
              return result.json();
            })
            .then((data) => {
              console.log(data);
              // Check if session ID is available
              if (data.sessionId) {
                // Redirect to Stripe Checkout
                return stripe.redirectToCheckout({ sessionId: data.sessionId });
              } else {
                // Handle error: session ID not available
                throw new Error("Checkout session ID is missing.");
              }
            })
            .then((res) => {
              console.log(res);
            })
            .catch((error) => {
              console.error("Error:", error.message);
            });
        });
      });