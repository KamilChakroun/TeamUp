# Multi-Step Signup Wizard - Visual Flow Diagram

## 📋 Complete Signup Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SIGNUP WIZARD FLOW                           │
└─────────────────────────────────────────────────────────────────┘

┌───────────────┐
│   START       │
│  /signup/     │
└───────┬───────┘
        │ Redirects
        ▼
┌──────────────────────────────────────────────────────────────────┐
│ STEP 1: Email Entry                                              │
│ URL: /users/signup/step1/                                        │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ 📧 Enter Email: [____________________]                   │   │
│ │                                                           │   │
│ │ Progress: ████████░░░░░░░░░░░░░░ 33%                    │   │
│ │                                                           │   │
│ │                                 [Next →]                 │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             │ Check Email Exists?
             ├─── Yes ──→ Redirect to Login ❌
             │
             └─── No ───→ Store in Session
                          │
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│ STEP 2: Account Details                                          │
│ URL: /users/signup/step2/                                        │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ Email: test@example.com (read-only)                      │   │
│ │                                                           │   │
│ │ 🔒 Password: [____________________]                      │   │
│ │ 🔒 Confirm:  [____________________]                      │   │
│ │                                                           │   │
│ │ 👤 Display Name (opt): [____________________]            │   │
│ │ 🏙️ City (opt): [____________________]                     │   │
│ │                                                           │   │
│ │ ⚽ Sports:                                                │   │
│ │    ☑ Football    ☑ Basketball    ☐ Tennis               │   │
│ │    ☐ Volleyball  ☐ Swimming      ☑ Running              │   │
│ │    ☐ Cycling     ☑ Gym/Fitness   ☐ Yoga                 │   │
│ │                                                           │   │
│ │ 📅 Availability:                                         │   │
│ │    [Weekdays after 6 PM, Weekends mornings_____]        │   │
│ │                                                           │   │
│ │ Progress: ████████████████░░░░░░░░ 66%                  │   │
│ │                                                           │   │
│ │ [← Back]                          [Continue →]          │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             │ Validate All Fields
             ├─── Invalid ──→ Show Errors, Stay on Page
             │
             └─── Valid ───→ Store in Session
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ STEP 3: Review & Confirm                                         │
│ URL: /users/signup/step3/                                        │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ ═══════════════════════════════════════════════════      │   │
│ │ 📋 ACCOUNT SUMMARY                                       │   │
│ │ ═══════════════════════════════════════════════════      │   │
│ │                                                           │   │
│ │ Email: test@example.com                                  │   │
│ │ Display Name: John Doe                                   │   │
│ │ City: New York                                           │   │
│ │                                                           │   │
│ │ Sports: [Football] [Basketball] [Running] [Gym]         │   │
│ │                                                           │   │
│ │ Availability: Weekdays after 6 PM, Weekends mornings    │   │
│ │                                                           │   │
│ │ ─────────────────────────────────────────────────        │   │
│ │ ℹ️  Email Verification Required                          │   │
│ │    We'll send a verification email to activate           │   │
│ │    your account.                                         │   │
│ │ ─────────────────────────────────────────────────        │   │
│ │                                                           │   │
│ │ ☑ I accept Terms & Conditions                           │   │
│ │                                                           │   │
│ │ Progress: ████████████████████████ 100%                 │   │
│ │                                                           │   │
│ │ [← Back]                    [✓ Create Account]          │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             │ On Submit
             ▼
┌──────────────────────────────────────────────────────────────────┐
│ BACKEND PROCESSING                                               │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ 1. Create User (is_active=False)                         │   │
│ │ 2. Hash Password                                         │   │
│ │ 3. Generate Username from Email                          │   │
│ │ 4. Create UserProfile (sports, availability)             │   │
│ │ 5. Generate EmailVerificationToken (UUID)                │   │
│ │ 6. Send Verification Email                               │   │
│ │ 7. Clear Session Data                                    │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────────────────────────┐
│ SUCCESS PAGE                                                     │
│ URL: /users/email-sent/                                          │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │        ✅                                                 │   │
│ │   CHECK YOUR EMAIL!                                       │   │
│ │                                                           │   │
│ │ We've sent a verification link to your email.            │   │
│ │                                                           │   │
│ │ Next Steps:                                              │   │
│ │ 1. Check your email inbox (and spam folder)              │   │
│ │ 2. Click the verification link                           │   │
│ │ 3. Your account will be activated                        │   │
│ │ 4. Log in and start connecting!                          │   │
│ │                                                           │   │
│ │ ⚠️ Verification link expires in 24 hours                 │   │
│ │                                                           │   │
│ │ Didn't receive? [Resend Verification Email]              │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             │ User checks email
             ▼
┌──────────────────────────────────────────────────────────────────┐
│ EMAIL RECEIVED                                                   │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ 🏆 Welcome to TeamUp!                                     │   │
│ │                                                           │   │
│ │ Hello John!                                               │   │
│ │                                                           │   │
│ │ Thank you for signing up for TeamUp!                     │   │
│ │                                                           │   │
│ │ Click to verify your email:                              │   │
│ │                                                           │   │
│ │         [Verify Email Address]                           │   │
│ │                                                           │   │
│ │ ⏰ Link expires in 24 hours                              │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             │ User clicks link
             ▼
┌──────────────────────────────────────────────────────────────────┐
│ EMAIL VERIFICATION                                               │
│ URL: /users/verify/<token>/                                      │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ Processing...                                             │   │
│ │                                                           │   │
│ │ 1. Find token in database                                │   │
│ │ 2. Check if valid (not used, not expired)                │   │
│ │ 3. Activate user (is_active=True)                        │   │
│ │ 4. Set email_verified_at timestamp                       │   │
│ │ 5. Mark token as used                                    │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             ├─── Token Invalid/Expired ──→ Show Error Page
             │                               with Resend Option
             │
             └─── Token Valid ───→ Activate Account
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────┐
│ ACTIVATION SUCCESS                                               │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ ✅ Email Verified Successfully!                           │   │
│ │                                                           │   │
│ │ You can now log in.                                      │   │
│ │                                                           │   │
│ │              [Go to Login →]                             │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────────────────────────┐
│ LOGIN PAGE                                                       │
│ URL: /users/login/                                               │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ Email: [____________________]                            │   │
│ │ Password: [____________________]                         │   │
│ │                                                           │   │
│ │              [Log In →]                                  │   │
│ └──────────────────────────────────────────────────────────┘   │
└────────────┬─────────────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────────────────────────┐
│ DASHBOARD                                                        │
│ URL: /dashboard/                                                 │
│ ┌──────────────────────────────────────────────────────────┐   │
│ │ 🎉 Welcome to TeamUp!                                     │   │
│ │                                                           │   │
│ │ You're now ready to:                                     │   │
│ │ • Find teammates                                         │   │
│ │ • Join sports events                                     │   │
│ │ • Create activities                                      │   │
│ │ • Build your community                                   │   │
│ └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

## 🔄 Alternative Paths

### If Email Already Exists:

```
Step 1: Enter Email
    ↓
Check Database
    ↓
Email Exists? YES
    ↓
❌ Show Error: "Account already exists"
    ↓
Redirect to Login Page
```

### If Token Expired:

```
Click Verification Link
    ↓
Check Token Validity
    ↓
Expired? YES
    ↓
❌ Show Error Page
    ↓
[Resend Verification] Button
    ↓
Generate New Token
    ↓
Send New Email
```

### Resend Verification Flow:

```
/users/resend-verification/
    ↓
Enter Email
    ↓
Find Inactive User
    ↓
Generate New Token
    ↓
Send Verification Email
    ↓
Success Message
```

## 📊 Data Storage Points

| Step   | Session Data                           | Database Data                    |
| ------ | -------------------------------------- | -------------------------------- |
| Step 1 | `signup_email`                         | None                             |
| Step 2 | + password, sports, availability, etc. | None                             |
| Step 3 | All data                               | User, UserProfile, Token created |
| Verify | Cleared                                | User activated                   |

## 🎨 UI Progress Indicators

```
Step 1: ████████░░░░░░░░░░░░░░ 33%
Step 2: ████████████████░░░░░░░░ 66%
Step 3: ████████████████████████ 100%
```

## 🔐 Security Checkpoints

1. ✅ Email uniqueness (Step 1)
2. ✅ Password validation (Step 2)
3. ✅ CSRF tokens (All forms)
4. ✅ Session validation (Step 2, 3)
5. ✅ Token validation (Verification)
6. ✅ Expiration check (Verification)
7. ✅ One-time use (Token marked as used)
8. ✅ Login requires active account
