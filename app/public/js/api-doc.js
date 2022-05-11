// The fallback fragment.
const FALLBACK_FRAGMENT = '#overview';

// An object that maps old fragments pointing to API info in the old API
// doc to new fragments pointing to API info in this API doc.
//
// NOTE: The following APIs are not listed as they were deprecated.
//
//   - '#client-extension-requestable_scopes-get-api'
//   - '#client-extension-requestable_scopes-update-api'
//   - '#client-extension-requestable_scopes-delete-api'
//
const API_FRAGMENT_MAP = {
  '#service-create-api'                      : '#post-/service/create',
  '#service/get-api'                         : '#get-/service/get/-serviceApiKey-',
  '#service-get-list-api'                    : '#get-/service/get/list',
  '#service-update-api'                      : '#post-/service/update/-serviceApiKey-',
  '#service-delete-api'                      : '#delete-/service/delete/-serviceApiKey-',
  '#client-create-api'                       : '#post-/client/create',
  '#client-get-api'                          : '#get-/client/get/-clientId-',
  '#client-get-list-api'                     : '#get-/client/get/list',
  '#client-update-api'                       : '#post-/client/update/-clientId-',
  '#client-delete-api'                       : '#delete-/client/delete/-clientId-',
  '#client-secret-refresh-api'               : '#post-/client/secret/refresh/-clientIdentifier-',
  '#client-secret-update-api'                : '#post-/client/secret/update/-clientIdentifier-',
  '#client-authorization-get-list-api'       : '#get-/client/authorization/get/list/-subject-',
  '#client-authorization-update-api'         : '#post-/client/authorization/update/-clientId-',
  '#client-authorization-delete-api'         : '#delete-/client/authorization/delete/-clientId-/-subject-',
  '#client-granted_scopes-get-api'           : '#get-/api/client/granted_scopes/get/-clientId-/-subject-',
  '#client-granted_scopes-delete-api'        : '#delete-/api/client/granted_scopes/delete/-clientId-/-subject-',
  '#auth-authorization-api'                  : '#post-/auth/authorization',
  '#auth-authorization-issue-api'            : '#post-/auth/authorization/issue',
  '#auth-authorization-fail-api'             : '#post-/auth/authorization/fail',
  '#auth-token-api'                          : '#post-/auth/token',
  '#auth-token-issue-api'                    : '#post-/auth/token/issue',
  '#auth-token-fail-api'                     : '#post-/auth/token/fail',
  '#auth-introspection-api'                  : '#post-/auth/introspection',
  '#auth-introspection-standard-api'         : '#post-/auth/introspection/standard',
  '#auth-revocation-api'                     : '#post-/auth/revocation',
  '#auth-userinfo-api'                       : '#post-/auth/userinfo',
  '#auth-userinfo-issue-api'                 : '#post-/auth/userinfo/issue',
  '#service-jwks-get-api'                    : '#get-/service/jwks/get',
  '#service-configuration-api'               : '#get-/service/configuration',
  '#client-registration-api'                 : '#post-/client/registration',
  '#client-registration-get-api'             : '#post-/client/registration/get',
  '#client-registration-update-api'          : '#post-/client/registration/update',
  '#client-registration-delete-api'          : '#post-/client/registration/delete',
  '#backchannel-authentication-api'          : '#post-/backchannel/authentication',
  '#backchannel-authentication-issue-api'    : '#post-/backchannel/authentication/issue',
  '#backchannel-authentication-fail-api'     : '#post-/backchannel/authentication/fail',
  '#backchannel-authentication-complete-api' : '#post-/backchannel/authentication/complete',
  '#device-authorization-api'                : '#post-/device/authorization',
  '#device-verification-api'                 : '#post-/device/verification',
  '#device-complete-api'                     : '#post-/device/complete',
  '#auth-token-get-list-api'                 : '#get-/auth/token/get/list',
  '#auth-token-create-api'                   : '#post-/auth/token/create',
  '#auth-token-update-api'                   : '#post-/auth/token/update',
  '#auth-token-delete-api'                   : '#delete-/auth/token/delete/-accessTokenIdentifier-',
  '#jose-verify-api'                         : '#post-/jose/verify'
};

const setupSwitchers = function () {
  // Set an event listener for the 'change' event on 'localeSwitcher'.
  getLocaleSwitcher().addEventListener('change', onSwitch);

  // Set an event listener for the 'change' event on 'documentSwitcher'.
  getDocumentSwitcher().addEventListener('change', onSwitch);
};

const onSwitch = function() {
  // Get the selected value from 'localeSwitcher'.
  const locale = getLocaleSwitcher().value;

  // Get the selected value from 'documentSwitcher'. The value is a
  // sub path that points to a specific version of document for a specific
  // server type (e.g. 'shared/2.2.1').
  const subPath = getDocumentSwitcher().value;

  // Redirect to the target path name.
  // NOTE: This doesn't change the current hash value.
  location.pathname = `/${locale}/${subPath}`;
};

const getLocaleSwitcher = function () {
  return document.getElementById('localeSwitcher');
};

const getDocumentSwitcher = function() {
  return document.getElementById('documentSwitcher');
};

const getApiDocElement = function() {
  return document.getElementById('apiDoc');
};

const checkFragment = function() {
  // The current fragment value.
  const currentFragment = location.hash;

  // Get a fragment value that replaces the current fragment value. This
  // value is a non-null value if replacement is necessary.
  const replacementFragment = getReplacementFragment(currentFragment);

  // Replace the current fragment value if necessary.
  if (replacementFragment)
  {
    location.hash = replacementFragment;
  }
};

const getReplacementFragment = function(currentFragment) {
  // If fragment value is not specified, set the current fragment value
  // to the fallback fragment value.
  if (!currentFragment)
  {
    return FALLBACK_FRAGMENT;
  }

  // Check if the current fragment value is valid.
  if (isValidFragment(currentFragment))
  {
    // OK. The current fragment value is valid. Then, it should not be
    // replaced.
    return null;
  }

  // The current frangment value is not valid but it could be a fragment
  // value used in the old API doc. The following code tries to replace
  // an old fragment value with the corresponding fragment value in this
  // API doc.

  // Check 1. Assume the current fragment value is an fragment value used
  // in the old API doc for pointing to an 'Authlete API'. And if that's
  // the case, replace it with the corresponding fragment value used in
  // this API doc.
  // For instance, '#service-create-api' is replaced with '#post-/service/create'.
  let newFragment = API_FRAGMENT_MAP[currentFragment];
  if (newFragment)
  {
    // OK. This means the assumption on check 1 is right. Then, the current
    // fragment value should be replaced with the new one.
    return newFragment;
  }

  // Check 2. Assume the current fragment value is an fragment value used
  // in the old API doc for pointing to an 'data type' (e.g. Service).
  // And if that's the case, replace it with the corresponding fragment
  // value used in this API doc.
  // For instance, '#access-token' is replaced with '#cmp--schemas-accesstoken'.
  newFragment = `#cmp--schemas-${currentFragment.substring(1).replace('-', '')}`
  if (isValidFragment(newFragment))
  {
    // OK. This means the assumption on check 2 is right. Then, the current
    // fragment value should be replaced with the new one.
    return newFragment;
  }

  // Check 3. Assume the current fragment value is a fragment value used
  // in the old API doc for pointing to an 'API result code'. And if
  // that's the case, replace it with the corresponding fragment value
  // used in this API doc.
  // For instance, '#A000101' is replaced with '#cmp--apiresultcode-A000101'.
  newFragment = `#cmp--apiresultcode-${currentFragment.substring(1).toLowerCase()}`;
  if (isValidFragment(newFragment))
  {
    // OK. This means the assumption on check 3 is right. Then, the current
    // fragment value should be replaced with the new one.
    return newFragment;
  }

  // The current fragment value is not valid and all the assumptions above
  // can't be applied. Then, return the fallback value.
  return FALLBACK_FRAGMENT;
};

const isValidFragment = function(fragment) {
  // We can't validate the fragment value by directly checking if the
  // API doc has an element that can be referenced by the fragment value
  // or not. This is because an element possibly doesn't exist in the
  // API doc unless the navigation item for the element gets clicked.
  // For instance, an element with id='A000001' doesn't exist in the API
  // doc unless the navigation element for that (an element with data-content-id='cmp--api-result-code-a000001')
  // gets clicked.
  // So, to validate the fragment value, we check if the API doc has the
  // navigation element for the element that can be referenced by the
  // fragment value.

  // Extract a content ID from the fragment value.
  const contentId = fragment.substring(1);

  // Check if a navigation element that has the content ID exists or not.
  return getNavigation(contentId);
};

const getNavigation = function(contentId) {
  return getNavigationSection().querySelector(`[data-content-id='${contentId}']`);
};

const getNavigationSection = function() {
  return getApiDocElement().shadowRoot.querySelector("[part='section-navbar-scroll']");
};

window.addEventListener('DOMContentLoaded', (e) => {
  // Set up switchers.
  setupSwitchers();

  // Add an event listener for 'spec-loaded' event.
  // NOTE: This must be done after ensuring that the DOM content is loaded.
  getApiDocElement().addEventListener('spec-loaded', (e) => {
    // Check the current fragment value and replace it if necessary.
    checkFragment();
  });
});