"""Generated client library for datastream version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.datastream.v1alpha1 import (
    datastream_v1alpha1_messages as messages,
)


class DatastreamV1alpha1(base_api.BaseApiClient):
    """Generated client library for service datastream version v1alpha1."""

    MESSAGES_MODULE = messages
    BASE_URL = "https://datastream.googleapis.com/"
    MTLS_BASE_URL = "https://datastream.mtls.googleapis.com/"

    _PACKAGE = "datastream"
    _SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
    _VERSION = "v1alpha1"
    _CLIENT_ID = "1042881264118.apps.googleusercontent.com"
    _CLIENT_SECRET = "x_Tw5K8nnjoRAqULM9PFAC2b"
    _USER_AGENT = "google-cloud-sdk"
    _CLIENT_CLASS_NAME = "DatastreamV1alpha1"
    _URL_VERSION = "v1alpha1"
    _API_KEY = None

    def __init__(
        self,
        url="",
        credentials=None,
        get_credentials=True,
        http=None,
        model=None,
        log_request=False,
        log_response=False,
        credentials_args=None,
        default_global_params=None,
        additional_http_headers=None,
        response_encoding=None,
    ):
        """Create a new datastream handle."""
        url = url or self.BASE_URL
        super(DatastreamV1alpha1, self).__init__(
            url,
            credentials=credentials,
            get_credentials=get_credentials,
            http=http,
            model=model,
            log_request=log_request,
            log_response=log_response,
            credentials_args=credentials_args,
            default_global_params=default_global_params,
            additional_http_headers=additional_http_headers,
            response_encoding=response_encoding,
        )
        self.projects_locations_connectionProfiles = self.ProjectsLocationsConnectionProfilesService(
            self
        )
        self.projects_locations_operations = self.ProjectsLocationsOperationsService(
            self
        )
        self.projects_locations_privateConnections_routes = self.ProjectsLocationsPrivateConnectionsRoutesService(
            self
        )
        self.projects_locations_privateConnections = self.ProjectsLocationsPrivateConnectionsService(
            self
        )
        self.projects_locations_streams = self.ProjectsLocationsStreamsService(self)
        self.projects_locations = self.ProjectsLocationsService(self)
        self.projects = self.ProjectsService(self)

    class ProjectsLocationsConnectionProfilesService(base_api.BaseApiService):
        """Service class for the projects_locations_connectionProfiles resource."""

        _NAME = "projects_locations_connectionProfiles"

        def __init__(self, client):
            super(
                DatastreamV1alpha1.ProjectsLocationsConnectionProfilesService, self
            ).__init__(client)
            self._upload_configs = {}

        def Create(self, request, global_params=None):
            r"""Use this method to create a connection profile in a project and location.

      Args:
        request: (DatastreamProjectsLocationsConnectionProfilesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Create")
            return self._RunMethod(config, request, global_params=global_params)

        Create.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/connectionProfiles",
            http_method="POST",
            method_id="datastream.projects.locations.connectionProfiles.create",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["connectionProfileId", "requestId"],
            relative_path="v1alpha1/{+parent}/connectionProfiles",
            request_field="connectionProfile",
            request_type_name="DatastreamProjectsLocationsConnectionProfilesCreateRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Delete(self, request, global_params=None):
            r"""Use this method to delete a connection profile..

      Args:
        request: (DatastreamProjectsLocationsConnectionProfilesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Delete")
            return self._RunMethod(config, request, global_params=global_params)

        Delete.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}",
            http_method="DELETE",
            method_id="datastream.projects.locations.connectionProfiles.delete",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["requestId"],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsConnectionProfilesDeleteRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Discover(self, request, global_params=None):
            r"""Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects under a parent data object that's optionally supplied in the request.

      Args:
        request: (DatastreamProjectsLocationsConnectionProfilesDiscoverRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DiscoverConnectionProfileResponse) The response message.
      """
            config = self.GetMethodConfig("Discover")
            return self._RunMethod(config, request, global_params=global_params)

        Discover.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/connectionProfiles:discover",
            http_method="POST",
            method_id="datastream.projects.locations.connectionProfiles.discover",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=[],
            relative_path="v1alpha1/{+parent}/connectionProfiles:discover",
            request_field="discoverConnectionProfileRequest",
            request_type_name="DatastreamProjectsLocationsConnectionProfilesDiscoverRequest",
            response_type_name="DiscoverConnectionProfileResponse",
            supports_download=False,
        )

        def Get(self, request, global_params=None):
            r"""Use this method to get details about a connection profile.

      Args:
        request: (DatastreamProjectsLocationsConnectionProfilesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ConnectionProfile) The response message.
      """
            config = self.GetMethodConfig("Get")
            return self._RunMethod(config, request, global_params=global_params)

        Get.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}",
            http_method="GET",
            method_id="datastream.projects.locations.connectionProfiles.get",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsConnectionProfilesGetRequest",
            response_type_name="ConnectionProfile",
            supports_download=False,
        )

        def List(self, request, global_params=None):
            r"""Use this method to list connection profiles created in a project and location.

      Args:
        request: (DatastreamProjectsLocationsConnectionProfilesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectionProfilesResponse) The response message.
      """
            config = self.GetMethodConfig("List")
            return self._RunMethod(config, request, global_params=global_params)

        List.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/connectionProfiles",
            http_method="GET",
            method_id="datastream.projects.locations.connectionProfiles.list",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["filter", "orderBy", "pageSize", "pageToken"],
            relative_path="v1alpha1/{+parent}/connectionProfiles",
            request_field="",
            request_type_name="DatastreamProjectsLocationsConnectionProfilesListRequest",
            response_type_name="ListConnectionProfilesResponse",
            supports_download=False,
        )

        def Patch(self, request, global_params=None):
            r"""Use this method to update the parameters of a connection profile.

      Args:
        request: (DatastreamProjectsLocationsConnectionProfilesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Patch")
            return self._RunMethod(config, request, global_params=global_params)

        Patch.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}",
            http_method="PATCH",
            method_id="datastream.projects.locations.connectionProfiles.patch",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["requestId", "updateMask"],
            relative_path="v1alpha1/{+name}",
            request_field="connectionProfile",
            request_type_name="DatastreamProjectsLocationsConnectionProfilesPatchRequest",
            response_type_name="Operation",
            supports_download=False,
        )

    class ProjectsLocationsOperationsService(base_api.BaseApiService):
        """Service class for the projects_locations_operations resource."""

        _NAME = "projects_locations_operations"

        def __init__(self, client):
            super(DatastreamV1alpha1.ProjectsLocationsOperationsService, self).__init__(
                client
            )
            self._upload_configs = {}

        def Cancel(self, request, global_params=None):
            r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (DatastreamProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
            config = self.GetMethodConfig("Cancel")
            return self._RunMethod(config, request, global_params=global_params)

        Cancel.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel",
            http_method="POST",
            method_id="datastream.projects.locations.operations.cancel",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}:cancel",
            request_field="cancelOperationRequest",
            request_type_name="DatastreamProjectsLocationsOperationsCancelRequest",
            response_type_name="Empty",
            supports_download=False,
        )

        def Delete(self, request, global_params=None):
            r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DatastreamProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
            config = self.GetMethodConfig("Delete")
            return self._RunMethod(config, request, global_params=global_params)

        Delete.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}",
            http_method="DELETE",
            method_id="datastream.projects.locations.operations.delete",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsOperationsDeleteRequest",
            response_type_name="Empty",
            supports_download=False,
        )

        def Get(self, request, global_params=None):
            r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (DatastreamProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Get")
            return self._RunMethod(config, request, global_params=global_params)

        Get.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}",
            http_method="GET",
            method_id="datastream.projects.locations.operations.get",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsOperationsGetRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def List(self, request, global_params=None):
            r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (DatastreamProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
            config = self.GetMethodConfig("List")
            return self._RunMethod(config, request, global_params=global_params)

        List.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/operations",
            http_method="GET",
            method_id="datastream.projects.locations.operations.list",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["filter", "pageSize", "pageToken"],
            relative_path="v1alpha1/{+name}/operations",
            request_field="",
            request_type_name="DatastreamProjectsLocationsOperationsListRequest",
            response_type_name="ListOperationsResponse",
            supports_download=False,
        )

    class ProjectsLocationsPrivateConnectionsRoutesService(base_api.BaseApiService):
        """Service class for the projects_locations_privateConnections_routes resource."""

        _NAME = "projects_locations_privateConnections_routes"

        def __init__(self, client):
            super(
                DatastreamV1alpha1.ProjectsLocationsPrivateConnectionsRoutesService,
                self,
            ).__init__(client)
            self._upload_configs = {}

        def Create(self, request, global_params=None):
            r"""Use this method to create a route for a private connectivity in a project and location.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsRoutesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Create")
            return self._RunMethod(config, request, global_params=global_params)

        Create.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections/{privateConnectionsId}/routes",
            http_method="POST",
            method_id="datastream.projects.locations.privateConnections.routes.create",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["requestId", "routeId"],
            relative_path="v1alpha1/{+parent}/routes",
            request_field="route",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsRoutesCreateRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Delete(self, request, global_params=None):
            r"""Use this method to delete a route.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsRoutesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Delete")
            return self._RunMethod(config, request, global_params=global_params)

        Delete.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections/{privateConnectionsId}/routes/{routesId}",
            http_method="DELETE",
            method_id="datastream.projects.locations.privateConnections.routes.delete",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["requestId"],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsRoutesDeleteRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Get(self, request, global_params=None):
            r"""Use this method to get details about a route.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsRoutesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Route) The response message.
      """
            config = self.GetMethodConfig("Get")
            return self._RunMethod(config, request, global_params=global_params)

        Get.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections/{privateConnectionsId}/routes/{routesId}",
            http_method="GET",
            method_id="datastream.projects.locations.privateConnections.routes.get",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsRoutesGetRequest",
            response_type_name="Route",
            supports_download=False,
        )

        def List(self, request, global_params=None):
            r"""Use this method to list routes created for a private connectivity in a project and location.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsRoutesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRoutesResponse) The response message.
      """
            config = self.GetMethodConfig("List")
            return self._RunMethod(config, request, global_params=global_params)

        List.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections/{privateConnectionsId}/routes",
            http_method="GET",
            method_id="datastream.projects.locations.privateConnections.routes.list",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["filter", "orderBy", "pageSize", "pageToken"],
            relative_path="v1alpha1/{+parent}/routes",
            request_field="",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsRoutesListRequest",
            response_type_name="ListRoutesResponse",
            supports_download=False,
        )

    class ProjectsLocationsPrivateConnectionsService(base_api.BaseApiService):
        """Service class for the projects_locations_privateConnections resource."""

        _NAME = "projects_locations_privateConnections"

        def __init__(self, client):
            super(
                DatastreamV1alpha1.ProjectsLocationsPrivateConnectionsService, self
            ).__init__(client)
            self._upload_configs = {}

        def Create(self, request, global_params=None):
            r"""Use this method to create a private connectivity configuration.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Create")
            return self._RunMethod(config, request, global_params=global_params)

        Create.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections",
            http_method="POST",
            method_id="datastream.projects.locations.privateConnections.create",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["privateConnectionId", "requestId"],
            relative_path="v1alpha1/{+parent}/privateConnections",
            request_field="privateConnection",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsCreateRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Delete(self, request, global_params=None):
            r"""Use this method to delete a private connectivity configuration.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Delete")
            return self._RunMethod(config, request, global_params=global_params)

        Delete.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections/{privateConnectionsId}",
            http_method="DELETE",
            method_id="datastream.projects.locations.privateConnections.delete",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["force", "requestId"],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsDeleteRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Get(self, request, global_params=None):
            r"""Use this method to get details about a private connectivity configuration.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PrivateConnection) The response message.
      """
            config = self.GetMethodConfig("Get")
            return self._RunMethod(config, request, global_params=global_params)

        Get.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections/{privateConnectionsId}",
            http_method="GET",
            method_id="datastream.projects.locations.privateConnections.get",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsGetRequest",
            response_type_name="PrivateConnection",
            supports_download=False,
        )

        def List(self, request, global_params=None):
            r"""Use this method to list private connectivity configurations in a project and location.

      Args:
        request: (DatastreamProjectsLocationsPrivateConnectionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPrivateConnectionsResponse) The response message.
      """
            config = self.GetMethodConfig("List")
            return self._RunMethod(config, request, global_params=global_params)

        List.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/privateConnections",
            http_method="GET",
            method_id="datastream.projects.locations.privateConnections.list",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["filter", "orderBy", "pageSize", "pageToken"],
            relative_path="v1alpha1/{+parent}/privateConnections",
            request_field="",
            request_type_name="DatastreamProjectsLocationsPrivateConnectionsListRequest",
            response_type_name="ListPrivateConnectionsResponse",
            supports_download=False,
        )

    class ProjectsLocationsStreamsService(base_api.BaseApiService):
        """Service class for the projects_locations_streams resource."""

        _NAME = "projects_locations_streams"

        def __init__(self, client):
            super(DatastreamV1alpha1.ProjectsLocationsStreamsService, self).__init__(
                client
            )
            self._upload_configs = {}

        def Create(self, request, global_params=None):
            r"""Use this method to create a stream.

      Args:
        request: (DatastreamProjectsLocationsStreamsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Create")
            return self._RunMethod(config, request, global_params=global_params)

        Create.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/streams",
            http_method="POST",
            method_id="datastream.projects.locations.streams.create",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["force", "requestId", "streamId", "validateOnly"],
            relative_path="v1alpha1/{+parent}/streams",
            request_field="stream",
            request_type_name="DatastreamProjectsLocationsStreamsCreateRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Delete(self, request, global_params=None):
            r"""Use this method to delete a stream.

      Args:
        request: (DatastreamProjectsLocationsStreamsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Delete")
            return self._RunMethod(config, request, global_params=global_params)

        Delete.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}",
            http_method="DELETE",
            method_id="datastream.projects.locations.streams.delete",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["requestId"],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsStreamsDeleteRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def FetchErrors(self, request, global_params=None):
            r"""Use this method to fetch any errors associated with a stream.

      Args:
        request: (DatastreamProjectsLocationsStreamsFetchErrorsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("FetchErrors")
            return self._RunMethod(config, request, global_params=global_params)

        FetchErrors.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}:fetchErrors",
            http_method="POST",
            method_id="datastream.projects.locations.streams.fetchErrors",
            ordered_params=["stream"],
            path_params=["stream"],
            query_params=[],
            relative_path="v1alpha1/{+stream}:fetchErrors",
            request_field="fetchErrorsRequest",
            request_type_name="DatastreamProjectsLocationsStreamsFetchErrorsRequest",
            response_type_name="Operation",
            supports_download=False,
        )

        def Get(self, request, global_params=None):
            r"""Use this method to get details about a stream.

      Args:
        request: (DatastreamProjectsLocationsStreamsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Stream) The response message.
      """
            config = self.GetMethodConfig("Get")
            return self._RunMethod(config, request, global_params=global_params)

        Get.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}",
            http_method="GET",
            method_id="datastream.projects.locations.streams.get",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsStreamsGetRequest",
            response_type_name="Stream",
            supports_download=False,
        )

        def List(self, request, global_params=None):
            r"""Use this method to list streams in a project and location.

      Args:
        request: (DatastreamProjectsLocationsStreamsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStreamsResponse) The response message.
      """
            config = self.GetMethodConfig("List")
            return self._RunMethod(config, request, global_params=global_params)

        List.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/streams",
            http_method="GET",
            method_id="datastream.projects.locations.streams.list",
            ordered_params=["parent"],
            path_params=["parent"],
            query_params=["filter", "orderBy", "pageSize", "pageToken"],
            relative_path="v1alpha1/{+parent}/streams",
            request_field="",
            request_type_name="DatastreamProjectsLocationsStreamsListRequest",
            response_type_name="ListStreamsResponse",
            supports_download=False,
        )

        def Patch(self, request, global_params=None):
            r"""Use this method to update the configuration of a stream.

      Args:
        request: (DatastreamProjectsLocationsStreamsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
            config = self.GetMethodConfig("Patch")
            return self._RunMethod(config, request, global_params=global_params)

        Patch.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}/streams/{streamsId}",
            http_method="PATCH",
            method_id="datastream.projects.locations.streams.patch",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["force", "requestId", "updateMask", "validateOnly"],
            relative_path="v1alpha1/{+name}",
            request_field="stream",
            request_type_name="DatastreamProjectsLocationsStreamsPatchRequest",
            response_type_name="Operation",
            supports_download=False,
        )

    class ProjectsLocationsService(base_api.BaseApiService):
        """Service class for the projects_locations resource."""

        _NAME = "projects_locations"

        def __init__(self, client):
            super(DatastreamV1alpha1.ProjectsLocationsService, self).__init__(client)
            self._upload_configs = {}

        def FetchStaticIps(self, request, global_params=None):
            r"""The FetchStaticIps API call exposes the static ips used by Datastream. Typically, a request returns children data objects under a parent data object that's optionally supplied in the request.

      Args:
        request: (DatastreamProjectsLocationsFetchStaticIpsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchStaticIpsResponse) The response message.
      """
            config = self.GetMethodConfig("FetchStaticIps")
            return self._RunMethod(config, request, global_params=global_params)

        FetchStaticIps.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}:fetchStaticIps",
            http_method="GET",
            method_id="datastream.projects.locations.fetchStaticIps",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["pageSize", "pageToken"],
            relative_path="v1alpha1/{+name}:fetchStaticIps",
            request_field="",
            request_type_name="DatastreamProjectsLocationsFetchStaticIpsRequest",
            response_type_name="FetchStaticIpsResponse",
            supports_download=False,
        )

        def Get(self, request, global_params=None):
            r"""Gets information about a location.

      Args:
        request: (DatastreamProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
            config = self.GetMethodConfig("Get")
            return self._RunMethod(config, request, global_params=global_params)

        Get.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations/{locationsId}",
            http_method="GET",
            method_id="datastream.projects.locations.get",
            ordered_params=["name"],
            path_params=["name"],
            query_params=[],
            relative_path="v1alpha1/{+name}",
            request_field="",
            request_type_name="DatastreamProjectsLocationsGetRequest",
            response_type_name="Location",
            supports_download=False,
        )

        def List(self, request, global_params=None):
            r"""Lists information about the supported locations for this service.

      Args:
        request: (DatastreamProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
            config = self.GetMethodConfig("List")
            return self._RunMethod(config, request, global_params=global_params)

        List.method_config = lambda: base_api.ApiMethodInfo(
            flat_path="v1alpha1/projects/{projectsId}/locations",
            http_method="GET",
            method_id="datastream.projects.locations.list",
            ordered_params=["name"],
            path_params=["name"],
            query_params=["filter", "pageSize", "pageToken"],
            relative_path="v1alpha1/{+name}/locations",
            request_field="",
            request_type_name="DatastreamProjectsLocationsListRequest",
            response_type_name="ListLocationsResponse",
            supports_download=False,
        )

    class ProjectsService(base_api.BaseApiService):
        """Service class for the projects resource."""

        _NAME = "projects"

        def __init__(self, client):
            super(DatastreamV1alpha1.ProjectsService, self).__init__(client)
            self._upload_configs = {}
