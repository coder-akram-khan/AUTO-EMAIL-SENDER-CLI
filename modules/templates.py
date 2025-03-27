"""
Templates module for Workerssal Mail Service
"""

def get_email_signature():
    """Return the HTML email signature"""
    return """<div style="width: 100%; max-width: 650px; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; margin: 0 auto; padding: 24px; background: linear-gradient(to right, #ffffff, #f7f9fc); border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);">
  <table style="width: 100%; border-collapse: collapse;">
    <tr>
      <td style="text-align: center; padding-bottom: 18px;">
        <h2 style="color: #4a6cf7; margin: 0; font-size: 22px; font-weight: 600; letter-spacing: -0.5px;">Workerssal</h2>
        <p style="color: #5d6b82; font-size: 13px; margin: 4px 0 0; font-weight: 400; letter-spacing: 0.2px;">Empowering Freelancers & Businesses</p>
      </td>
    </tr>
    
    <tr>
      <td style="padding: 0 0 18px;">
        <div style="height: 2px; background: linear-gradient(to right, #4a6cf7, #6e8fff); border-radius: 2px;"></div>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; padding-bottom: 16px;">
        <p style="margin: 0; color: #2c3444; font-size: 15px; font-weight: 500;">Best Regards,</p>
        <p style="margin: 3px 0 0; font-size: 15px; color: #3a4356;">The Workerssal Team</p>
      </td>
    </tr>
    <!-- Social Links -->
    <tr>
      <td style="text-align: center; padding-bottom: 18px;">
        <table style="margin: 0 auto;">
          <tr>
            <td style="padding: 4px;">
              <a href="https://workerssal.com" style="display: inline-block; text-decoration: none; font-size: 13px; color: #4a6cf7; font-weight: 500; padding: 6px 10px; border-radius: 4px; background-color: rgba(74, 108, 247, 0.1);">
                🌐 Website
              </a>
            </td>
            <td style="padding: 4px;">
              <a href="https://linkedin.com/company/workerssal" style="display: inline-block; text-decoration: none; font-size: 13px; color: #0A66C2; font-weight: 500; padding: 6px 10px; border-radius: 4px; background-color: rgba(10, 102, 194, 0.1);">
                🔗 LinkedIn
              </a>
            </td>
            <td style="padding: 4px;">
              <a href="https://instagram.com/workerssal" style="display: inline-block; text-decoration: none; font-size: 13px; color: #E4405F; font-weight: 500; padding: 6px 10px; border-radius: 4px; background-color: rgba(228, 64, 95, 0.1);">
                📷 Instagram
              </a>
            </td>
            <td style="padding: 4px;">
              <a href="https://x.com/workerssal" style="display: inline-block; text-decoration: none; font-size: 13px; color: #000000; font-weight: 500; padding: 6px 10px; border-radius: 4px; background-color: rgba(0, 0, 0, 0.1);">
                ✖ Twitter
              </a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td style="text-align: center;">
        <p style="font-size: 13px; color: #5d6b82; margin: 0; font-weight: 400;">
          🚀 Transforming Ideas into Success
        </p>
      </td>
    </tr>
  </table>
</div>"""

def get_brand_email_template(company):
    """Return HTML formatted brand email template with modern aesthetic design"""
    return f"""
    <div style="color: #2c3444; font-size: 16px; line-height: 1.6;">
        <!-- Header with gradient background -->
        <div style="background: linear-gradient(135deg, #4a6cf7 0%, #6e8fff 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; text-align: center;">
            <h1 style="color: white; margin: 0; font-size: 24px; font-weight: 600; letter-spacing: -0.5px;">Brand Collaboration Opportunity</h1>
            <p style="color: rgba(255, 255, 255, 0.9); margin: 8px 0 0; font-size: 15px;">Connect with the perfect influencers for your brand</p>
        </div>
        
        <!-- Personalized greeting -->
        <p style="font-size: 18px; font-weight: 600; color: #4a6cf7; margin-bottom: 16px; padding-left: 5px; border-left: 4px solid #4a6cf7;">
            Hey {company} team,
        </p>
        
        <!-- Main content with nice typography -->
        <div style="background-color: #f8fafc; padding: 22px; border-radius: 10px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);">
            <p style="margin-top: 0;">Looking to get your products/services in front of the right audience? At <span style="color: #4a6cf7; font-weight: 600;">Workerssal</span>, we connect brands with top influencers who can drive real engagement and sales for you.</p>
        </div>
        
        <!-- Feature list with enhanced styling -->
        <div style="margin: 25px 0; background: linear-gradient(to right, #ffffff, #f7f9fc); border-radius: 12px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); padding: 5px;">
            <div style="padding: 18px; border-bottom: 1px solid rgba(74, 108, 247, 0.15);">
                <p style="margin: 8px 0; display: flex; align-items: center;">
                    <span style="background-color: #4a6cf7; color: white; margin-right: 15px; font-size: 14px; height: 24px; width: 24px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">✓</span> 
                    <span style="font-weight: 500;">Handpicked influencers in your niche</span>
                </p>
            </div>
            
            <div style="padding: 18px; border-bottom: 1px solid rgba(74, 108, 247, 0.15);">
                <p style="margin: 8px 0; display: flex; align-items: center;">
                    <span style="background-color: #4a6cf7; color: white; margin-right: 15px; font-size: 14px; height: 24px; width: 24px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">✓</span> 
                    <span style="font-weight: 500;">Authentic promotions that build trust</span>
                </p>
            </div>
            
            <div style="padding: 18px;">
                <p style="margin: 8px 0; display: flex; align-items: center;">
                    <span style="background-color: #4a6cf7; color: white; margin-right: 15px; font-size: 14px; height: 24px; width: 24px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">✓</span> 
                    <span style="font-weight: 500;">End-to-end campaign management – zero hassle for you</span>
                </p>
            </div>
        </div>
        
        <!-- Call to action -->
        <div style="text-align: center; margin: 30px 0 15px; padding: 25px; background-color: rgba(74, 108, 247, 0.05); border-radius: 10px;">
            <p style="font-weight: 600; font-size: 17px; color: #2c3444; margin-bottom: 15px;">Let's discuss how we can bring you the perfect influencers for your brand.</p>
            <p style="color: #4a6cf7; font-weight: 600; font-size: 18px;">When's a good time to chat? 📅</p>
        </div>
    </div>
    """

def get_influencer_email_template(username):
    """Return HTML formatted influencer email template with modern aesthetic design"""
    return f"""
    <div style="color: #2c3444; font-size: 16px; line-height: 1.6;">
        <!-- Header with gradient background -->
        <div style="background: linear-gradient(135deg, #4a6cf7 0%, #6e8fff 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; text-align: center;">
            <h1 style="color: white; margin: 0; font-size: 24px; font-weight: 600; letter-spacing: -0.5px;">Paid Brand Deals Await</h1>
            <p style="color: rgba(255, 255, 255, 0.9); margin: 8px 0 0; font-size: 15px;">Focus on content, we'll bring the sponsors</p>
        </div>
        
        <!-- Personalized greeting -->
        <p style="font-size: 18px; font-weight: 600; color: #4a6cf7; margin-bottom: 16px; padding-left: 5px; border-left: 4px solid #4a6cf7;">
            Hey {username},
        </p>
        
        <!-- Modern card layout -->
        <div style="background-color: #f8fafc; padding: 22px; border-radius: 10px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);">
            <p style="margin-top: 0;">We're helping influencers like you land paid brand deals—without the stress of outreach or negotiations.</p>
        </div>
        
        <!-- Value proposition -->
        <div style="margin: 25px 0; background: linear-gradient(to right, #ffffff, #f7f9fc); border-radius: 12px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); padding: 22px; position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; width: 5px; height: 100%; background: linear-gradient(to bottom, #4a6cf7, #6e8fff);"></div>
            
            <div style="padding-left: 15px;">
                <h3 style="color: #4a6cf7; margin-top: 0; font-size: 18px; font-weight: 600;">How It Works:</h3>
                <p style="margin-bottom: 10px;">At <span style="color: #4a6cf7; font-weight: 600;">Workerssal</span>, we connect you with top brands that fit your niche, so you can:</p>
                
                <ul style="list-style-type: none; padding-left: 5px; margin: 15px 0;">
                    <li style="margin-bottom: 12px; display: flex; align-items: center;">
                        <span style="color: #4a6cf7; margin-right: 10px; font-size: 18px;">•</span>
                        <span>Focus on creating amazing content</span>
                    </li>
                    <li style="margin-bottom: 12px; display: flex; align-items: center;">
                        <span style="color: #4a6cf7; margin-right: 10px; font-size: 18px;">•</span>
                        <span>Skip the tedious outreach process</span>
                    </li>
                    <li style="display: flex; align-items: center;">
                        <span style="color: #4a6cf7; margin-right: 10px; font-size: 18px;">•</span>
                        <span>Get matched with brands that truly value your audience</span>
                    </li>
                </ul>
            </div>
        </div>
        
        <!-- Call to action -->
        <div style="text-align: center; margin: 30px 0 15px; padding: 25px; background: rgba(74, 108, 247, 0.05); border-radius: 10px;">
            <p style="font-weight: 600; font-size: 18px; margin-bottom: 0; color: #2c3444;">Interested? Let's get you paid! <span style="font-size: 22px;">💰</span></p>
            <p style="margin-top: 15px; font-size: 15px; color: #4a6cf7;">Reply to this email or visit <a href="https://workerssal.com" style="color: #4a6cf7; font-weight: 600; text-decoration: none;">workerssal.com</a> to get started</p>
        </div>
    </div>
    """ 