Name:           ros-indigo-combine-dr-measurements
Version:        0.1.2
Release:        1%{?dist}
Summary:        ROS combine_dr_measurements package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf

%description
The combine_dr_measurements package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Apr 28 2015 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.2-1
- Autogenerated by Bloom

* Mon Dec 29 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.2-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-1
- Autogenerated by Bloom

* Wed Dec 17 2014 Daiki Maekawa <method_aspect_card@yahoo.co.jp> - 0.1.1-2
- Autogenerated by Bloom

