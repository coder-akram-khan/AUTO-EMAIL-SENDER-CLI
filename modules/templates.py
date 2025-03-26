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
    """Return HTML formatted brand email template"""
    return f"""
    <div style="color: #2c3444; font-size: 16px; line-height: 1.6;">
        <p style="font-size: 18px; font-weight: 600; color: #4a6cf7; margin-bottom: 16px;">Hey {company} team,</p>
        
        <p>Looking to get your products/services in front of the right audience? At <span style="color: #4a6cf7; font-weight: 500;">Workersal</span>, we connect brands with top influencers who can drive real engagement and sales for you.</p>
        
        <div style="margin: 20px 0; padding: 15px; background-color: rgba(74, 108, 247, 0.05); border-left: 4px solid #4a6cf7; border-radius: 4px;">
            <p style="margin: 8px 0; display: flex; align-items: center;">
                <span style="color: #4a6cf7; margin-right: 10px; font-size: 18px;">✅</span> 
                <span>Handpicked influencers in your niche</span>
            </p>
            <p style="margin: 8px 0; display: flex; align-items: center;">
                <span style="color: #4a6cf7; margin-right: 10px; font-size: 18px;">✅</span> 
                <span>Authentic promotions that build trust</span>
            </p>
            <p style="margin: 8px 0; display: flex; align-items: center;">
                <span style="color: #4a6cf7; margin-right: 10px; font-size: 18px;">✅</span> 
                <span>End-to-end campaign management – zero hassle for you</span>
            </p>
        </div>
        
        <p>Let's discuss how we can bring you the perfect influencers for your brand. When's a good time to chat?</p>
    </div>
    """

def get_influencer_email_template(username):
    """Return HTML formatted influencer email template"""
    return f"""
    <div style="color: #2c3444; font-size: 16px; line-height: 1.6;">
        <p style="font-size: 18px; font-weight: 600; color: #4a6cf7; margin-bottom: 16px;">Hey {username},</p>
        
        <p>We're helping influencers like you land paid brand deals—without the stress of outreach or negotiations.</p>
        
        <div style="margin: 20px 0; padding: 15px; background-color: rgba(74, 108, 247, 0.05); border-left: 4px solid #4a6cf7; border-radius: 4px;">
            <p>At <span style="color: #4a6cf7; font-weight: 500;">Workersal</span>, we connect you with top brands that fit your niche, so you can focus on content while we bring the sponsorships to you.</p>
        </div>
        
        <p style="font-weight: 500;">Interested? Let's get you paid!! 💰</p>
    </div>
    """ 